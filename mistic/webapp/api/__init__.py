# -*- coding: utf-8 -*-
from flask import Blueprint

from mistic import configs

blueprint = Blueprint(name='api_blueprint',
                      import_name=__name__,
                      url_prefix=configs['FLASK_APP_ROOT_URL'] + 'api',
                      )
