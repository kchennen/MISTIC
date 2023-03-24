# -*- coding: utf-8 -*-
import os

from flask import Blueprint, render_template
from requests import get

from mistic import configs

blueprint = Blueprint(name='base_blueprint',
                      import_name=__name__,
                      url_prefix=configs['FLASK_APP_ROOT_URL'],
                      template_folder='templates',
                      static_folder='static'
                      )


@blueprint.route('/')
def home():
    return render_template('home.html', title='Home')


@blueprint.route('/download')
def download():
    return render_template('download.html', title='Download')


@blueprint.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')


@blueprint.route('/config')
def config():
    from mistic.webapp.api.routes import api
    url = os.path.join(api.base_url, 'swagger.json')
    response = get(url)

    api_config = response.json()
    api_config['basePath'] = api.base_url[:-1]

    return api_config
