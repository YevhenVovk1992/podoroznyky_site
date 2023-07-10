import os

import dotenv

app_dir = os.path.abspath(os.path.dirname(__file__))

# Loading environment variables into the project
dotenv_path = os.path.join(app_dir, '.flaskenv')
dotenv.load_dotenv(dotenv_path)


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
