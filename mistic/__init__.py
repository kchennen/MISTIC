# -*- coding: utf-8 -*-
import logging
import multiprocessing
import os
import time
import yaml as yaml

start_time = time.time()
logger = logging.getLogger(__name__)
num_cores = multiprocessing.cpu_count()  # Determine the number of threads for Parallel run

with open(os.path.join(os.path.dirname(__file__), "configs.yaml"), "r") as f:
    configs = yaml.load(stream=f, Loader=yaml.FullLoader)
    if configs['FLASK_APP_DEBUG']:
        configs['log_level'] = logging.DEBUG
    else:
        configs['log_level'] = logging.INFO

# Initialize project parameters
prog_name = configs['project']
logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] - {prog_name} - %(levelname)s - %(message)s'.format(prog_name=prog_name),
                    datefmt='%Y-%m-%d %H:%M:%S')
