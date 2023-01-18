import requests
import json
import os
from .api import *
from .testbreed import *
from flask import Flask, render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def user():
        return render_template('index.html', img=img, breeds=breeds)
    @app.route('/doggo')
    def hello():
        response_API = requests.get('https://dog.ceo/api/breeds/image/random')
        data=response_API.text
        parse_json=json.loads(data)
        img=parse_json["message"]
        return render_template('doggo.html', img=img, breeds=breeds)
    @app.route('/doggo/<path:breed>')
    def getbreed(breed):
        if breed in breeds:
            response_API = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')
            data=response_API.text
            parse_json=json.loads(data)
            img=parse_json["message"] 
            print(img)
            print(parse_json)
            return render_template('doggo.html', img=img, breeds=breeds)
        else: return ('NOOOO')
    @app.route('/history')
    def history():
        return render_template('history.html', img=img)
    @app.route('/random')
    def random():
        response_API2 = requests.get(f'https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1')
        data2=response_API2.text
        parse_json2=json.loads(data2)
        fact=parse_json2["fact"] 
        return render_template('random.html', fact=fact)

    return app

