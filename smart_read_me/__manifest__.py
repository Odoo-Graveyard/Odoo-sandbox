# -*- coding: utf-8 -*-
{
    'name': "smart_read_me",  # Module title
    'summary': "read me",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Hinamizawa",
    'website': "https://github.com/alejandroatacho",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base', 'website', 'web'],
    # 'icon': '/my_library/static/icon.png',
    'data': [
        'views/home.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            'smart_read_me/static/src/css/my_library.css',
            'smart_read_me/static/src/scss/my_library.scss'
        ],
    },
    'qweb': [
        'static/src/views/templates.xml'
    ]

}
