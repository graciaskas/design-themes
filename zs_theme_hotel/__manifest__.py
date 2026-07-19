# -*- coding: utf-8 -*-
{
    'name': 'Hotel',
    'description': 'Design moderne et épuré pour la gestion hôtelière.',
    'version': '17.0.0.1',
    'category': 'Website/Theme',
    'author': 'Gracias Kasongo',
    'depends': ["theme_common"],
    'data': [
        
    ],
   'assets': {
        # 1. On charge d'abord les variables de couleur
        'web._assets_primary_variables': [
            'zs_theme_hotel/static/src/scss/primary_variables.scss',
        ],
        # 2. On charge ensuite le style général
        'web.assets_frontend': [
            'zs_theme_hotel/static/src/scss/bootstrap_overrides.scss',
            'zs_theme_hotel/static/src/scss/theme.scss',
        ],
    },
    'images': [
        'static/description/theme_cover.jpg',
        'static/description/theme_screenshot.jpg',
    ],
   
    'configurator_snippets': {
        'homepage':[]
    },
}