# -*- coding: utf-8 -*-
{
    'name': "ZhongYi",

    'summary': """
        中医""",

    'description': """
        中医
    """,

    'author': "Tony",
    'website': "http://www.wffeitas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm','sale','purchase','stock','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/product.xml',
        'views/res_partner.xml',
        'views/crm_lead_views.xml',
        'views/sale_views.xml',
        'views/linchuang.xml',

        'views/menu_action.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}