# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLineStockQuant(models.Model):
    _inherit = "sale.order.line"

    def open_stock_quant_popup(self):
        # Ensure that there is a product associated with this sale order line
        if self.product_id:
            # Retrieve stock quants related to the product
            stock_quants = (
                self.env["stock.quant"]
                .sudo()
                .search(
                    [
                        ("product_id", "=", self.product_id.id),
                        ("location_id.usage", "=", "internal"),
                        ("quantity", ">", 0.0),
                    ],
                    order="removal_date DESC",
                )
            )

            # Create a list of stock.quant IDs for the domain filter
            stock_quant_ids = stock_quants.ids

            # Return an action to open the stock.quant popup
            return {
                "name": "Stock Quant Popup",
                "view_type": "form",
                "view_mode": "tree,form",
                "res_model": "stock.quant",
                "type": "ir.actions.act_window",
                "domain": [
                    ("id", "in", stock_quant_ids),
                ],
                "target": "new",
            }
        else:
            # Handle the case where there's no product associated with the sale order line
            return {
                "type": "ir.actions.client",
                "tag": "warning",
                "name": "Product Not Found",
                "message": "No product associated with this sale order line.",
            }
