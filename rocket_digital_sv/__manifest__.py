# -*- coding: utf-8 -*-
{
    'name': "Rocket Digital",

    'summary': """
        Rocket Digital""",

    'description': """
       Modificar Codigo de sistema
    """,

    'author': "Rocket Digital",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_config_views.xml',
     #   'views/doctype_html.xml',
        'views/view_icon_tm.xml',
        'views/template_inherit_layout.xml',
        'views/templates_inherit_contact.xml',
        'views/views.xml',
        'views/templates.xml'
       

        
    ],
    'assets': {
        'web.assets_backend_prod_only': [
            'rocket_digital_sv/static/src/js/favicon.js',
        ],
    },
    'assets': {
        'web.assets_frontend': [
            'rocket_digital_sv/static/src/css/**/*',
        ]
    },
    # only loaded in demonstration mode
   # 'demo': [
    #    'demo/demo.xml',
    #],
    'images': [
        'static/description/tree.jpg',
        
    ],
}
