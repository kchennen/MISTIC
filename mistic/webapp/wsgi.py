import subprocess

from mistic import configs
from mistic.webapp import create_app

app = create_app()


def run(host=configs['FLASK_APP_HOST'], port=configs['FLASK_APP_PORT']):
    app.run(host=host,
            port=port,
            )


def wsgi(webapp='mistic.webapp.wsgi:run', host='0.0.0.0', port=configs['FLASK_APP_PORT'], workers=1):
    bash_cmd = 'uvicorn --host {h} '.format(h=host) + \
               '--port {p} '.format(p=port) + \
               '--workers {w} '.format(w=workers) + \
               '{a}'.format(a=webapp)

    subprocess.run(args=bash_cmd.split(), stdout=subprocess.PIPE)
