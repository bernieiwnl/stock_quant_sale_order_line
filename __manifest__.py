# -*- coding: utf-8 -*-
{
    "name": "Sale Order Line Stock Quant",
    "summary": """Get pop up form view of stock quantity in sale order line""",
    "description": """Get pop up form view of stock quantity in sale order line""",
    "author": "Agustian Suhartono",
    "website": "berniecxy@gmail.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Sales",
    "version": "0.1",
    "application": True,
    "installable": True,
    # any module necessary for this one to work correctly
    "depends": ["base", "sale", "stock"],
    # always loaded
    "data": [
        # 'views\sale_order_line_stock_quant.xml',
        "views\stock_quant_tree_removal_date.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
}
