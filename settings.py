from path import path

ROOT_DIR =  path(__file__).parent
APPS_DIR = ROOT_DIR / 'apps'

DEBUG = True

SSH_ID_PATH = ''

try:
    from deploy_settings import *
except:
    pass
