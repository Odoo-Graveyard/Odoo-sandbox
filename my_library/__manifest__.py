# -*- coding: utf-8 -*-
{
    'name': "My Library",  # Module title
    'summary': "Manage books easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Hinamizawa",
    'website': "https://github.com/alejandroatacho",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base','website','web'],
    'icon': '/my_library/static/icon.png',
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        # 'views/library_template.xml',
    ],  
    'installable': True,
    'auto_install': True,
    'application': False,
    'sequence': 1,
    'auto_update': True,
    'assets': {
        'web.assets_frontend': [
            # 'my_library/static/src/js/library.js',
            'my_library/static/src/css/views.css',
        ],
    },

    # This demo data files will be loaded if db initialize with demo data (commented because file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
