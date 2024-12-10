# Copyright 2015-2021 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    invoice_import_ids = fields.One2many(
        "account.invoice.import.config",
        "partner_id",
        string="Invoice Import Configuration",
    )
    invoice_import_count = fields.Integer(
        compute="_compute_invoice_import_count",
        string="Number of Invoice Import Configurations",
        readonly=True,
    )

    def _compute_invoice_import_count(self):
        config_data = self.env["account.invoice.import.config"].read_group(
            [("partner_id", "in", self.ids), ("company_id", "=", self.env.company.id)],
            ["partner_id"],
            ["partner_id"],
        )
        mapped_data = {
            config["partner_id"][0]: config["partner_id_count"]
            for config in config_data
        }
        for partner in self:
            partner.invoice_import_count = mapped_data.get(partner.id, 0)

    def show_account_invoice_import_config(self):
        self.ensure_one()
        action = self.env["ir.actions.act_window"].for_xml_id(
            "account_invoice_import", "account_invoice_import_config_action"
        )
        action["context"] = {
            "default_name": self.name,
            "default_partner_id": self.id,
            "search_default_partner_id": self.id,
            "invoice_import_config_main_view": True,
        }
        return action

    def _get_e_invoice_vat_search_args(self, vat, wildcard_vat):
        """
        Return default search query for partner search by vat
        """
        normalized_vat = vat.replace(" ", "")
        return [
            ("vat", "in", [normalized_vat, vat]),
            ("tax_number", "in", [normalized_vat, vat]),
        ]

    def _get_e_invoice_tax_number_search_args(self, tax_number, wildcard_tax_number):
        """
        Return default search query for partner search by tax_number in e invoice
        """
        normalized_tax_number = tax_number.replace(" ", "")
        return [
            ("vat", "in", [normalized_tax_number, tax_number]),
            ("tax_number", "in", [normalized_tax_number, tax_number]),
        ]

    def _get_e_invoice_gln_search_args(self, gln, wildcard_gln):
        """
        Return default search query for partner search by gln in e invoice
        """
        PartnerIDNumber = self.env["res.partner.id_number"]
        normalized_gln = gln.replace(" ", "")
        partner_ids = PartnerIDNumber.search(
            [
                ("active", "=", True),
                ("category_id.code", "=", "gln_id_number"),
                ("name", "in", [normalized_gln, gln]),
            ]
        ).mapped("partner_id")
        if partner_ids:
            return [("id", "in", partner_ids.ids)]
        return []
