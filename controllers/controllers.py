# -*- coding: utf-8 -*-
from odoo import http

# class SaleOrderLineStockQuant(http.Controller):
#     @http.route('/sale_order_line_stock_quant/sale_order_line_stock_quant/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_line_stock_quant/sale_order_line_stock_quant/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_line_stock_quant.listing', {
#             'root': '/sale_order_line_stock_quant/sale_order_line_stock_quant',
#             'objects': http.request.env['sale_order_line_stock_quant.sale_order_line_stock_quant'].search([]),
#         })

#     @http.route('/sale_order_line_stock_quant/sale_order_line_stock_quant/objects/<model("sale_order_line_stock_quant.sale_order_line_stock_quant"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_line_stock_quant.object', {
#             'object': obj
#         })