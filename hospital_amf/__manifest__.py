# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': "Modulo para un hospital",

    'description': """
Modulo para un hospital
    """,

    'author': "AdrianMF",
    'website': "https://www.youtube.com/watch?v=NK4sboUQqtc",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/diagnosis_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

