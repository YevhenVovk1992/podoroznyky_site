from flask import request, render_template, Blueprint, g, abort, current_app


multilingual = Blueprint('multilingual', __name__, template_folder='templates', url_prefix='/<lang_code>')


@multilingual.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)


@multilingual.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')


@multilingual.before_request
def before_request():
    if g.lang_code not in current_app.config['LANGUAGES']:
        abort(404)


@multilingual.route('/')
@multilingual.route('/index/')
def index():
    """
    The function renders start page.
    """
    return render_template('multilingual/index.html', title='Home')


@multilingual.route('/contacts/')
def contact_view():
    """
    The function renders page of contacts.
    """
    return render_template('multilingual/contact.html', title='Contacts')


@multilingual.route('/photo/')
def photo_view():
    """
    The function renders page with images.
    """
    return render_template('multilingual/photos.html', title='Photos')
