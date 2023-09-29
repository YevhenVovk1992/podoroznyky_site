import os

from flask import Flask, request, g, redirect, url_for
from flask_babel import Babel
from flask_sitemap import Sitemap

import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig if os.environ.get('DEBUG') else config.ProductionConfig)
ext = Sitemap(app=app)
app.config['SITEMAP_URL_SCHEME'] = 'https'

# import and register blueprints
from app.blueprints.multilingual import multilingual, errors

app.register_blueprint(multilingual)


def do_not_set_russian(land_code: str) -> str:
    if land_code == 'ru':
        return 'uk'
    return land_code


# set up babel
def get_locale():
    if not g.get('lang_code', None):
        user_language = request.accept_languages.best_match(app.config['LANGUAGES'])
        g.lang_code = do_not_set_russian(user_language)
    return g.lang_code


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home():
    get_locale()
    return redirect(url_for('multilingual.index'))


@ext.register_generator
def sitemap():
    """
    Sitemap urls
    :return: XML response
    """
    land_code_list = config.BaseConfig.LANGUAGES
    for land_code in land_code_list:
        g.lang_code = land_code
        yield 'multilingual.index', {}
        yield 'multilingual.contact_view', {}
        yield 'multilingual.photo_view', {}


