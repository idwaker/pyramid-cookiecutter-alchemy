"""Pyramid bootstrap environment.

Place 'pyramid_config_file' into alembic.ini, and the application will
be loaded from there.

"""
from alembic import context
from paste.deploy import loadapp
from pyramid.paster import get_appsettings, setup_logging
from sqlalchemy import engine_from_config


config = context.config
# can use config['__file__'] here, i.e. the Pyramid
# ini file, instead of alembic.ini
CONFIG_FILE = config.get_main_option('pyramid_config_file')

setup_logging(CONFIG_FILE)

app = loadapp('config:%s' % CONFIG_FILE, relative_to='.')
settings = get_appsettings(CONFIG_FILE)

# customize this section for non-standard engine configurations.
target_metadata = __import__(app.registry.__name__).models.meta.Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(settings.get('sqlalchemy.url'))
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # specify here how the engine is acquired
    engine = engine_from_config(settings, 'sqlalchemy.')

    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
