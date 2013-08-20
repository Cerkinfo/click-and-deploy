from fabric.api import run, cd, env
from fabric import state

DISTANT_PATH = 'testing'

def pull():
    with cd(DISTANT_PATH):
        run('git pull')

def restart_services():
    print 'restarting some things'
    #run('sudo supervisorctl restart ' + ' '.join(PROCESSES))

def deploy():
    pull()
    restart_services()
