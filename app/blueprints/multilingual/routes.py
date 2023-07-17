import json
import os

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
    All images are stored in '../app/static/img/' link.
    """

    # Search all images in a folder. Group them into 3 groups.
    comment_text = None
    base_dir = os.path.abspath(os.curdir)
    land_code = g.lang_code
    images_list = os.listdir(base_dir + '/app/static/img/photos/')
    n = len(images_list)//3
    list_for_template = [images_list[i:i + n] for i in range(0, len(images_list), n)]

    # Reading signatures for images from a file. Choice of translation depending on the user's language.
    with open(base_dir + '/app/img_text.json', 'r', encoding='utf-8') as file:
        json_text = file.read()
    multilingual_text = json.loads(json_text)
    if land_code == 'en':
        comment_text = multilingual_text.get('en')
    elif land_code == 'uk':
        comment_text = multilingual_text.get('uk')

    return render_template(
        'multilingual/photos.html',
        title='Photos',
        content={'images_list': list_for_template, 'comment_text': comment_text}
    )
