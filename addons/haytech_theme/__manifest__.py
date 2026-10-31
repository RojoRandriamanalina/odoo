{
    'name': 'Thème HayTech',
    'summary': 'Charte graphique HayTech (couleurs, polices, logo) pour Odoo',
    'version': '20.0.1.0.0',
    'category': 'Theme/Backend',
    'author': 'HayTech',
    'website': 'https://haytech.stream',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'views/webclient_templates.xml',
        'data/company.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'haytech_theme/static/src/scss/primary_variables.scss'),
        ],
        'web.assets_backend': [
            'haytech_theme/static/src/scss/fonts.scss',
            'haytech_theme/static/src/scss/backend.scss',
        ],
        'web.assets_frontend': [
            'haytech_theme/static/src/scss/fonts.scss',
            'haytech_theme/static/src/scss/login.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': True,
}
