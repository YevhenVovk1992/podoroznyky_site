import os

from flask import Flask, request, g, redirect, url_for
from flask_babel import Babel

import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig if os.environ.get('DEBUG') else config.ProductionConfig)

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
    user_language = request.accept_languages.best_match(app.config['LANGUAGES'])
    g.lang_code = do_not_set_russian(user_language)
    return redirect(url_for('multilingual.index'))
