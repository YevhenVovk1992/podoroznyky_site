import os

from flask import Flask, request, g, redirect, url_for
from flask_babel import Babel

import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig if os.environ.get('DEBUG') else config.ProductionConfig)

# import and register blueprints
from app.blueprints.multilingual import multilingual, errors

app.register_blueprint(multilingual)


# set up babel
def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return g.lang_code


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home():
    g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
    return redirect(url_for('multilingual.index'))
