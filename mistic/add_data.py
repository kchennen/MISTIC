#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import sys
import time

pathname = os.path.dirname(sys.argv[0])
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.join(pathname, '..'))

from mistic import configs

logger = logging.getLogger(__name__)


def fetch_data():
    static_data = os.path.join(pathname,
                               'webapp', 'base', 'static', 'data')

    root_path = configs['FLASK_APP_RES']['root_path']
    res_files = configs['FLASK_APP_RES']['download']
    
    for r in res_files:
        print(os.path.join(root_path, res_files[r]),
                   os.path.join(static_data, res_files[r]))
        os.symlink(os.path.join(root_path, res_files[r]),
                   os.path.join(static_data, res_files[r]))


if __name__ == '__main__':
    START_TIME = time.time()
    # Set logging config
    logging.basicConfig(level=configs['log_level'],
                        format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='{}_flask.log'.format(configs['FLASK_APP_NAME']))
    fetch_data()

    END_TIME = time.time()
    sys.stdout.write('Done in {}s\n'.format(round(number=(END_TIME - START_TIME), ndigits=3)))
