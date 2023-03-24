#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import sys
import time

from webapp import create_app

pathname = os.path.dirname(sys.argv[0])
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.join(pathname, '..'))

from mistic import configs

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    START_TIME = time.time()
    # Set logging config
    logging.basicConfig(level=configs['log_level'],
                        format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='{}_flask.log'.format(configs['FLASK_APP_NAME']))
    web_app = create_app()
    web_app.run(host='0.0.0.0',
                port=configs['FLASK_APP_PORT'],
                )

    END_TIME = time.time()
    sys.stdout.write('Done in {}s\n'.format(round(number=(END_TIME - START_TIME), ndigits=3)))
