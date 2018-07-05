
from flask import Flask
from flask_bootstrap import Bootstrap

from config import config
from app.main import main as main_blueprint

def create_app(config_name):
    app = Flask(__name__)
    Bootstrap(app)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.register_blueprint(main_blueprint)

    return app
