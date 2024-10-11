# -*- coding: utf-8 -*-
{
    'name': "owl ",
    'summary': """ owl dashboard """,
    'description': """ owl dashboard""",
    'sequence':-200,
    'author': "Class",
    'website': "http://www.yourcompany.com",
    'category': '',
    'version': '0.1',
    'depends': ['base','web','sale','board'],
    'data': [
        'views/sales_dashboard.xml',
    ],
    'demo': [],
    'application':True,
    'auto_install': False,
    'licence':'LGPL-3',
    'assets':{
        'web.assets_backend':[
            'owl/static/src/components/**/*.js',
            'owl/static/src/components/**/*.xml',
            'owl/static/src/components/**/*.scss',
        ]
    }
}
