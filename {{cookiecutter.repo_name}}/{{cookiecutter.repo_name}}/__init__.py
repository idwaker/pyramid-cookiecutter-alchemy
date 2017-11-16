from os import environ

from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy

from {{cookiecutter.repo_name}}.managers import init_logging


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # initialize services
    init_logging(config)

    # set authorization policy and enable JWT authentication
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.include('pyramid_jwt')
    # key-accessor is there so that it throws exception if the key is not set
    config.set_jwt_authentication_policy(environ['{{cookiecutter.repo_name.upper()}}_SECRET_KEY'])

    # includes
    config.include('cornice')
    config.include('.models')
    config.include('.routes')
    config.scan()

    return config.make_wsgi_app()
