import json
import os

from flask import request, render_template, Blueprint, g, abort, current_app

from utils import paginator as PG


multilingual = Blueprint('multilingual', __name__, template_folder='templates', url_prefix='/<lang_code>')


def group_list_element(data_list: list, n: int = 3):
    """
    The function groups the elements in a list. Adds them in increments equal to the number of groups
    :param data_list: list with data
    :param n: integer, how many elements was in the group
    :return: a new list with items grouped into lists
    """
    result = []
    for i in range(n):
        cash_list = []
        for el in range(0, len(data_list), n):
            try:
                cash_list.append(data_list[el + i])
            except IndexError:
                pass
        result.append(cash_list.copy())
    return result


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
    base_dir = os.path.abspath(os.curdir)
    banner_list = os.listdir(base_dir + '/app/static/img/banners/')
    return render_template(
        'multilingual/index.html',
        title='Home',
        content={
            'banner': banner_list
        }
    )


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
    base_dir = os.path.abspath(os.curdir)
    land_code = g.lang_code
    images_list = os.listdir(base_dir + '/app/static/img/photos/')
    images_list.sort(reverse=True)

    # Pagination images and group by 3 column
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1
    paginator = PG.CustomPaginator(page, images_list, 18)
    data_list = paginator.get_data()
    list_for_template = group_list_element(data_list)

    # Reading signatures for images from a file. Choice of translation depending on the user's language.
    comment_text = None
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
        content={
            'images_list': list_for_template,
            'comment_text': comment_text,
            'paginator': paginator
        }
    )
