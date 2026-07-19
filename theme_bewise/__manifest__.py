{
    'name': 'Theme: Hotel Luxury',
    'description': 'Luxury Hotel Theme for Odoo 17',
    'category': 'Theme/Hotel',
    'summary': 'Hotel, Resort, Rooms, Booking, Luxury',
    'version': '17.0.1.0.0',
    'depends': ['theme_common'], # Très important pour hériter des styles de base
    'data': [
        'data/zs_ir_asset.xml',
        'views/zs_snippets.xml',
        'views/zs_new_page_template.xml', # Pour proposer des modèles de pages pré-faits
    ],
    'images': [
        'static/description/zs_hotel_description.jpg',
        'static/description/zs_hotel_screenshot.jpg',
    ],
    # Prévisualisation des images pour les snippets par défaut
    'images_preview_theme': {
        'website.s_cover_default_image': '/zs_theme_hotel/static/src/img/hero_hotel.jpg',
        'website.s_text_image_default_image': '/zs_theme_hotel/static/src/img/room_preview.jpg',
    },
    # Définit quels blocs apparaissent sur la page d'accueil par défaut
    'configurator_snippets': {
        'homepage': ['s_cover', 's_text_image', 's_image_text', 's_quotes_carousel'],
    },
    'license': 'LGPL-3',
    'assets': {
        'web.assets_frontend': [
            'zs_theme_hotel/static/src/scss/zs_style.scss',
        ],
    }
}