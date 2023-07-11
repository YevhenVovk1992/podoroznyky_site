from flask import request, render_template, Blueprint, g
from flask_babel import _, refresh

from app import app


multilingual = Blueprint('multilingual', __name__, template_folder='templates')


@multilingual.route('/')
@multilingual.route('/index')
def index():
    """
    The function renders start page.
    """
    # g.lang_code = 'en'
    # refresh()
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