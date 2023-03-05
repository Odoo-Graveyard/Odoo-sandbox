{
    'name': 'My Website',
    'depends': ['base', 'website', 'web'],
    'data': [
        'views/home.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_frontend': [
            'hina_web/static/src/css/main.css',
            'hina_web/static/src/js/web_calc.js',
        ],
    },
}
