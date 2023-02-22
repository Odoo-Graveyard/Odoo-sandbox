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
    'depends': ['website'],
    # 'icon': '/my_library/static/icon.png',
    'data': [
    ],  
    'installable': True,
    'auto_install': True,
    'application': False,
    'sequence': 1,
    'auto_update': True,
    'assets': {
        'web.assets_frontend': [
            'my_library/static/src/css/views.css',
        ],
    },
'qweb': [
    'static/src/xml/*.xml',
],

}
