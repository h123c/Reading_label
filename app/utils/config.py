#encoding:utf-8
import os

#import redis
from flask import Flask

from app.main.views import user_blueprint
#from App.models import db


def create_app():
	#/aicoding/app
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir)

    app.register_blueprint(blueprint=user_blueprint, url_prefix='/reading_label')

    return app

if __name__ == "__main__":
    print(root_path)