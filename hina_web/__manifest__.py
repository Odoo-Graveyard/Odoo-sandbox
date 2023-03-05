{
    'name': 'My Website Injector',
    'version': '1.0',
    'category': 'Website',
    'summary': 'My Website Injector for XML/SASS/JS/Python',
    'description': 'My Website Injector for XML/SASS/JS/Python',
    'author': 'Hinamizawa (alejandroatacho)',
    'website': 'https://github.com/alejandroatacho',
    'license': 'AGPL-3',
    'images': ['static/src/img/hinamizawa.png'],
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
