from odoo import models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _get_e_invoice_default_code_search_args(
        self, default_code, wildcard_default_code
    ):
        """
        Return default search query for product search by default code in e invoice
        """
        return [("default_code", "=", default_code)]

    def _get_e_invoice_barcode_search_args(self, barcode, wildcard_barcode):
        """
        Return default search query for product search by barcode in e invoice
        """
        return [("barcode", "=", barcode)]
