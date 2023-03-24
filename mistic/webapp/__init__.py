# -*- coding: utf-8 -*-
import logging
import os
from flask import Flask

from mistic import configs
from mistic.webapp import base, api
from mistic.webapp.utils.environments import Environments


def register_extensions(app):
    # Load configs
    configs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'configs.yaml')
    env = Environments(app)
    env.from_yaml(configs_path)
    

def register_blueprints(app):
    app.register_blueprint(base.blueprint)
    app.register_blueprint(api.blueprint)


def configure_logs(app, level=logging.INFO):
    logging.basicConfig(level=level,
                        format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        )
    logger = logging.getLogger(app.config['FLASK_APP_NAME'])
    logger.addHandler(logging.StreamHandler())


def create_app():
    web_app = Flask(__name__, static_folder='base/static')
    
    register_extensions(web_app)
    register_blueprints(web_app)
    configure_logs(web_app,
                   level=configs['log_level'])
    
    return web_app
