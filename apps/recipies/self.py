from fabric.api import run, cd, env
from fabric import state

DISTANT_PATH = '/www-data/click-and-deploy'

def pull():
    with cd(DISTANT_PATH):
        run('git pull')

def restart_services():
    run('sudo supervisorctl restart click-and-deploy')

def deploy():
    pull()
    restart_services()
