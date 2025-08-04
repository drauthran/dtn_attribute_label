# -*- coding: utf-8 -*-
{
    'name': "DTN Attribute Label (40x58)",
    'summary': """
        Adds a custom product label (40x58mm) with SKU, Name, Price, Barcode, and Product Attributes.
        Overrides Dymo label template for custom layout.
        """,
    'author': "Drauthran",
    'version': '1.0',
    'category': 'Inventory/Inventory',
    'depends': ['stock', 'product'],
    'data': [
        'views/report_paperformat.xml',
        'views/report_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}