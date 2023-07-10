import os

from flask import Flask

import config


app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig if os.environ.get('DEBUG') else config.ProductionConfig)

from app.blueprints.multilingual import multilingual, errors

app.register_blueprint(multilingual)

