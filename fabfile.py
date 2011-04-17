from fabric.api import local
import os

#Assumes that the code is cloned from git@github.com:asldevi/django-mongodb.git and you are in the django-mongo dir

def install(dir='zesty'):
    local('python setup.py develop')

def mongo(dbdir='data'):
    """locals mongodb server.
        
    assumes that mongo is in the $PATH
    """
    if not os.path.exists(dbdir):
        os.mkdir(dbdir)
    local('mongod --dbpath %s' % dbdir)

def django(bind_addr="0.0.0.0:8000"):
    """locals django development server
    """
    local('python manage.py syncdb')
    local('python manage.py runserver %s' % bind_addr)
