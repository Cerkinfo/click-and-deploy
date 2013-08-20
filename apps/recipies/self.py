from fabric.api import run, cd, env
from fabric import state

DISTANT_PATH = 'click-and-deploy'

def pull():
    with cd(DISTANT_PATH):
        run('git pull')

def restart_services():
    run('sudo supervisorctl restart deploy:deploy-web')

def deploy():
    pull()
    restart_services()
