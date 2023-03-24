import time

import click as click
import click_log
from mistic.webapp import wsgi

from mistic import configs, logger, start_time


@click.group()
@click.version_option(version='0.1')
def cli():
    """MISTIC CLI"""
    pass


@cli.command()
@click.option('--host', '-h',
              type=str,
              default=configs['FLASK_APP_HOST'],
              required=False,
              help='Host server name. Default = \'{h}\'.'.format(h=configs['FLASK_APP_HOST']))
@click.option('--port', '-p',
              type=int,
              default=configs['FLASK_APP_PORT'],
              help='Server port. Default = {p}.'.format(p=configs['FLASK_APP_PORT']))
@click_log.simple_verbosity_option(logger)
def run(host, port):
    """Run webapp via Uvicorn"""
    wsgi.wsgi(host=host, port=port)

    end_time = time.time()
    click.echo('Done in {}s\n'.format(round(number=(end_time - start_time), ndigits=3)))


@cli.command()
@click.option('--host', '-h',
              type=str,
              default=configs['FLASK_APP_HOST'],
              required=False,
              help='Host server name. Default = \'{h}\'.'.format(h=configs['FLASK_APP_HOST']))
@click.option('--port', '-p',
              type=int,
              default=configs['FLASK_APP_PORT'],
              help='Server port. Default = {p}.'.format(p=configs['FLASK_APP_PORT']))
@click_log.simple_verbosity_option(logger)
def flask(host, port):
    """Run webapp via Flask"""
    wsgi.run(host=host, port=port)

    end_time = time.time()
    click.echo('Done in {}s\n'.format(round(number=(end_time - start_time), ndigits=3)))
