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
    'depends': ['base','website'],
    # 'icon': '/my_library/static/icon.png',
    'data': [
    ],  
    'installable': True,
    'auto_install': True,
    'application': False,
    'sequence': 1,
    'auto_update': True,
    'views': ['/my_library/static/src/xml/home.xml'],
    'assets': {
        'web.assets_frontend': [
            'my_library/static/src/css/my_library.css',
            'my_library/static/src/scss/my_library.scss'
        ],
    },
'qweb': [
    'static/src/xml/*.xml',
],

}
