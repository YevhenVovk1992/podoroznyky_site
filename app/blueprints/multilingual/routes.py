from flask import request, render_template, Blueprint

from app import app


multilingual = Blueprint('multilingual', __name__, template_folder='templates')


@multilingual.route('/')
@multilingual.route('/index')
# @app.route('/', methods=['GET', ])
def index():
    """
    The function renders start page.
    """
    return render_template('multilingual/index.html', title='Home')


# @app.route('/contacts/', methods=['GET', ])
@multilingual.route('/contacts/')
def contact_view():
    """
    The function renders page of contacts.
    """
    return render_template('multilingual/contact.html', title='Contacts')


# @app.route('/photo/', methods=['GET', ])
@multilingual.route('/photo/')
def photo_view():
    """
    The function renders page with images.
    """
    return render_template('multilingual/photos.html', title='Photos')