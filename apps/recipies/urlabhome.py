from fabric.api import run, cd, env
from fabric import state

DISTANT_PATH = 'homepage'

def pull_update():
    with cd(DISTANT_PATH):
        run('git pull')
        run('/home/homepage/homepage/ve/bin/pip install -r requirements.txt')

def restart_services():
    run('sudo supervisorctl restart homepage')

def gen_graphs():
    run('/home/homepage/homepage/openings_cron_script.sh')

def deploy():
    pull_update()
    restart_services()
    gen_graphs()
