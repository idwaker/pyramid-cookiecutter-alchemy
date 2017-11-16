from pyramid.config import Configurator
from {{cookiecutter.repo_name}}.managers import init_logging


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # initialize services
    init_logging(config)

    # includes
    config.include('.models')
    config.include('.routes')
    config.scan()

    return config.make_wsgi_app()
