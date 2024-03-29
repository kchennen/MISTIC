# -*- coding: utf-8 -*-
import logging
import os
import yaml
from flask import current_app


class Environments(object):
    
    def __init__(self, app=None, var_name=None, default_env=None):
        self.app = app
        self.var_name = var_name or 'FLASK_ENV'
        self.default_env = default_env or 'DEVELOPMENT'
        self.env = os.environ.get(self.var_name, self.default_env)
        
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        app.config['ENVIRONMENT'] = self.env
        
        if app.extensions is None:
            app.extensions = {}
        
        app.extensions['environments'] = self
    
    def get_app(self, reference_app=None):
        if reference_app is not None:
            return reference_app
        if self.app is not None:
            return self.app
        return current_app
    
    def from_object(self, config_obj):
        app = self.get_app()
        
        for name in self._possible_names():
            try:
                obj = '%s.%s' % (config_obj, name)
                app.config.from_object(obj)
                return
            except Exception as e:
                logging.exception(e)
        
        app.config.from_object(config_obj)
    
    def from_yaml(self, path):
        with open(path) as f:
            c = yaml.load(f, Loader=yaml.FullLoader)
        
        for name in self._possible_names():
            try:
                c = c[name]
            except KeyError:
                pass
        
        app = self.get_app()
        
        for key in c:
            if key.isupper():
                app.config[key] = c[key]
    
    def _possible_names(self):
        return self.env.lower(), self.env.capitalize(), self.env.upper()
