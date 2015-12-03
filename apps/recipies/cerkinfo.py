from fabric.api import run, cd, env
from fabric.context_managers import prefix


def deploy():
    code_dir = '/www-data/cerkinfo_site'
    with cd(code_dir), prefix('source .ve/bin/activate'):
        run('sudo supervisorctl stop cerkinfo_site')
        run("git pull")
        run("pip install -r requirements.txt --upgrade -q")
        run("./manage.py collectstatic --noinput -v 0")
        run("./manage.py makemigrations")
        run("./manage.py migrate")
        run('sudo supervisorctl start cerkinfo_site')