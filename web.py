from flask import Flask, render_template, abort
from path import path
import settings
import lib
from rq import Connection, Queue
from redis import Redis

flapp = Flask(__name__)
flapp.debug = settings.DEBUG


redis_conn = Redis()
q = Queue(connection=redis_conn)


@flapp.route("/")
def hello():
    files = settings.APPS_DIR.listdir('*.app')
    apps = map(lambda app_file : lib.json_to_app(app_file), files)
    return render_template('hello.html', apps=apps)

@flapp.route("/app/<app_id>/")
def show_app(app_id):
    app = lib.app_id_to_data(app_id)
    return render_template('app.html', app=app)

@flapp.route("/app/<app_id>/deploy/", methods=['GET', 'POST'])
def deploy_app(app_id):
    lib.app_exists(app_id)
    job = q.enqueue(lib.deploy_app, app_id)
    return ("Deployment added in queue, should be ok soon.<br>"
        +'<a href=".">Go back to app</a>')


if __name__ == "__main__":
    flapp.run()