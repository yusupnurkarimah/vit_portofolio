# -*- coding: utf-8 -*-
{
    'name': "vit_portofolio",

    'summary': """
        My Portofolio
        """,

    'description': """
        My Portofolio
    """,

    'author': "yusup[vitraining.com]",
    'website': "http://github.com/yusupnurkarimah",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','website'],

    # always loaded
    'data': [
        'data/group.xml',
        'views/views.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}