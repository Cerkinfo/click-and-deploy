from path import path
import random
import settings
import json
import  importlib
import fabric.tasks
from flask import abort

def app_exists(app_id):
    app_file = settings.APPS_DIR / (app_id + '.app')
    if not app_file.exists():
        abort(404)
    return app_file

def app_id_to_data(app_id):
    app_file = app_exists(app_id)
    app = json_to_app(app_file)
    return app

def json_to_app(app_path):
    try:
        j = json.loads(app_path.text())
    except:
        if settings.DEBUG:
            abort(500,"JSON must be bad")
        else:
            abort(500)
    j['id'] = app_path.name[:-len(app_path.ext)]
    return j

def deploy_app(app_id):
    app = app_id_to_data(app_id)
    fabfile = importlib.import_module('apps.recipies.'+app_id)
    fabfile.env.hosts = app['target']

    fabric.tasks.execute(fabfile.deploy)
    (path('/tmp') / str(random.randint(0,10))).touch()