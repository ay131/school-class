# -*- coding: utf-8 -*-
{
    'name': "School Class",
    'author': "",
    'website': "",
    'category': 'Odoo',
    'version': '0.1',
    'depends': ['contacts'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',

        'views/school_class_view.xml',
        'views/school_subject_view.xml',
        'views/menu_action.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': -100,

}
