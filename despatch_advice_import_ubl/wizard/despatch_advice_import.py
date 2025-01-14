# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import _, api, models
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class DespatchAdviceImport(models.TransientModel):

    _name = "despatch.advice.import"
    _inherit = ["despatch.advice.import", "base.ubl"]

    @api.model
    def parse_xml_despatch_advice(self, xml_root):
        start_tag = "{urn:oasis:names:specification:ubl:schema:xsd:"
        if xml_root.tag == start_tag + "DespatchAdvice-2}DespatchAdvice":
            return self.parse_ubl_despatch_advice(xml_root)
        else:
            return super(DespatchAdviceImport, self).parse_xml_despatch_advice(xml_root)

    @api.model
    def parse_ubl_despatch_advice(self, xml_root):
        ns = xml_root.nsmap
        # Get main xmlns
        if None in ns:
            main_xmlns = ns.pop(None)
        else:
            main_xmlns = ns.pop("DespatchAdvice")
        ns["main"] = main_xmlns
        date_el = xml_root.xpath("/main:DespatchAdvice/cbc:IssueDate", namespaces=ns)
        estimated_delivery_date_el = xml_root.xpath(
            "/main:DespatchAdvice/cac:Shipment/cac:Delivery/"
            "cac:EstimatedDeliveryPeriod/cbc:EndDate",
            namespaces=ns,
        )
        order_id_el = xml_root.xpath("/main:DespatchAdvice/cbc:ID", namespaces=ns)
        order_reference_el = xml_root.xpath(
            "/main:DespatchAdvice/cac:OrderReference/cbc:ID", namespaces=ns
        )

        despatch_advice_type_code_el = xml_root.xpath(
            "/main:DespatchAdvice/cbc:DespatchAdviceTypeCode", namespaces=ns
        )

        supplier_el = xml_root.xpath(
            "/main:DespatchAdvice/cac:DespatchSupplierParty/cac:Party", namespaces=ns
        )
        # We only take the "official references" for supplier_dict
        supplier_dict = self.ubl_parse_party(supplier_el[0], ns)
        supplier_dict = {
            "vat": supplier_dict.get("vat"),
        }
        customer_el = xml_root.xpath(
            "/main:DespatchAdvice/cac:DeliveryCustomerParty/cac:Party", namespaces=ns
        )
        customer_dict = self.ubl_parse_party(customer_el[0], ns)

        customer_dict = {"vat": customer_dict.get("vat")}
        lines_el = xml_root.xpath(
            "/main:DespatchAdvice/cac:DespatchLine", namespaces=ns
        )
        res_lines = []
        for line in lines_el:
            res_lines.append(self.parse_ubl_despatch_advice_line(line, ns))
        res = {
            "id": order_id_el[0].text if order_id_el else "",
            "ref": order_reference_el[0].text if order_reference_el else "",
            "supplier": supplier_dict,
            "company": customer_dict,
            "despatch_advice_type_code": (
                despatch_advice_type_code_el[0].text
                if len(despatch_advice_type_code_el) > 0
                else ""
            ),
            "date": len(date_el) and date_el[0].text,
            "estimated_delivery_date": len(estimated_delivery_date_el)
            and estimated_delivery_date_el[0].text,
            "lines": res_lines,
        }
        return res

    @api.model
    def parse_ubl_despatch_advice_line(self, line, ns):
        line_id_el = line.xpath("cbc:ID", namespaces=ns)
        qty_el = line.xpath("cbc:DeliveredQuantity", namespaces=ns)
        qty = float(qty_el[0].text)
        backorder_qty_el = line.xpath("cbc:OutstandingQuantity", namespaces=ns)
        backorder_qty = None
        if backorder_qty_el and len(backorder_qty_el):
            backorder_qty = float(backorder_qty_el[0].text)
        else:
            backorder_qty = 0

        product_ref_el = line.xpath(
            "cac:Item/cac:SellersItemIdentification/cbc:ID", namespaces=ns
        )

        if len(product_ref_el) == 0:
            product_ref_el = line.xpath(
                "cac:Item/cac:BuyersItemIdentification/cbc:ID", namespaces=ns
            )

        product_lot_el = line.xpath(
            "cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID",
            namespaces=ns,
        )
        order_reference_el = line.xpath(
            "cac:OrderLineReference/cac:OrderReference/cbc:ID", namespaces=ns
        )

        order_line_id_el = line.xpath(
            "cac:OrderLineReference/cbc:LineID", namespaces=ns
        )

        if not order_line_id_el:
            raise UserError(_("Missing line ID in the Despatch Advice."))

        res_line = {
            "line_id": line_id_el[0].text,
            "order_line_id": order_line_id_el[0].text,
            "ref": order_reference_el[0].text if order_reference_el else "",
            "qty": qty,
            "product_ref": product_ref_el[0].text,
            "product_lot": product_lot_el[0].text if product_lot_el else "",
            "uom": {"unece_code": qty_el[0].attrib.get("unitCode")},
            "backorder_qty": backorder_qty,
        }

        package_id_el = line.xpath(
            "cac:Shipment/cac:TransportHandlingUnit/cac:ActualPackage/cbc:ID",
            namespaces=ns,
        )
        package_type_el = line.xpath(
            "cac:Shipment/cac:TransportHandlingUnit/cbc:TransportHandlingUnitTypeCode",
            namespaces=ns,
        )
        package_weight_el = line.xpath(
            "cac:Shipment/cac:GrossWeightMeasure/cbc:Measure", namespaces=ns
        )
        if package_id_el or package_type_el:
            res_line["package"] = {
                "name": package_id_el[0].text if package_id_el else "",
                "type": package_type_el[0].text if package_type_el else "",
                "weight": package_weight_el[0].text if package_weight_el else "",
            }

        defaults = self.env.context.get("despatch_advice_import__default_vals", {}).get(
            "lines", {}
        )
        res_line.update(defaults)
        return res_line

    @api.model
    def ubl_parse_party(self, party_node, ns):
        partner_name_el = party_node.xpath("cac:PartyName/cbc:Name", namespaces=ns)
        if not partner_name_el:
            partner_name_el = party_node.xpath(
                "cac:PartyLegalEntity/cbc:RegistrationName", namespaces=ns
            )

        vat_el = party_node.xpath("cac:PartyIdentification/cbc:ID", namespaces=ns)
        partner_dict = {
            "vat": (
                vat_el[0].text
                if vat_el and vat_el[0].attrib.get("schemeName").upper()
                else False
            ),
            "name": partner_name_el[0].text,
        }
        address_el = party_node.xpath("cac:PostalAddress", namespaces=ns)
        if address_el:
            address_dict = self.ubl_parse_address(address_el[0], ns)
            partner_dict.update(address_dict)
        return partner_dict
