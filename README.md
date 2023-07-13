# Podoroznyky web site
### Multilingual web site written in flask framework.
Link - 
___
![podoroznyky_screen_1](https://github.com/YevhenVovk1992/BenzinCheck/assets/104986485/215910f7-c781-4b59-98bf-c3ab298d98f5)
![podoroznyky_screen_2](https://github.com/YevhenVovk1992/BenzinCheck/assets/104986485/b5a6a9aa-3a15-44e1-8a37-98aa2bfc9651)
![podoroznyky_screen_3](https://github.com/YevhenVovk1992/BenzinCheck/assets/104986485/18eca57c-dc07-4fc1-b2ba-85f527a23de3)
___
## Content
 - [Technologies](#what-we-used)
 - [Desription](#what-we-do)
 - [Star Project](#how-to-start-project)
 - [Sources](#sources)

___
## What we used?
_Technologies used_: Flask, Flask-babel, html, css, js

## What we do?
Create an API in Python, which implements a single endpoint that accepts syntactic input
tree of the English text and returns its paraphrased versions:
 - path: /paraphrase
 - HTTP method: GET
 - query parameters:
   - tree: str (required) – a syntactic tree in the form of a string (see example below)
   - limit: int (optional, default: 20) - the maximum number of paraphrased texts that
response must be returned: a list of paraphrased trees in JSON format.


## How to start project?
1. Run `git clone {SSH-link from GitHub}` on your PC;
2. Run `pip install -r requirements.txt`;
3. Create '.flaskenv' file and write to it environment variables:
	- SECRET_KEY (Fot example: '*jfjn&nf8jfghg=fgkhd6k56566');
	- DEBUG=1 for development;
    - FLASK_APP=runner.py;
4. Run `python3 runner.py`;

<h6>If information has been added to the site that needs to be translated, the following instructions will help you.</h6>
If we want to scan files, restore the layout in the file, to translate the text, this is done using the command
inside the root folder of our environment:
`pybabel extract -F babel.cfg -o messages.pot .`<br>
This generates the messages.pot file which can be recompiled every time we need to update our translations and therefore 
also should be excluded from versioning.
Now we want to create our translation files where we manually need to translate all the text we extracted from our files. 
These files will be created inside the app/translations folder and are generated with the following command:
`pybabel init -i messages.pot -d app/translations -l uk`<br>
This creates the file for the Ukraine translation. Our next task is to go to app/translations , open the *.po files and 
translate all the text in the respective language.
Once this tedious work is over with, we can compile all of our translations with the command:
`pybabel compile -d app/translations`<br>

## Sources
1. [The Flask Mega-Tutorial Part XIII](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
2. [Flask, Create a Multilingual Web Application with Language Specific URL’s](https://medium.com/@nicolas_84494/flask-create-a-multilingual-web-application-with-language-specific-urls-5d994344f5fd)