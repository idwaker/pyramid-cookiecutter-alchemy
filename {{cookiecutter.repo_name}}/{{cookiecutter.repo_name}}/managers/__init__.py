from .logbook_manager import init_logbook


def init_logging(config):
    """
    """
    settings = config.get_settings()
    log_level = settings.get('log_level')
    log_filename = settings.get('log_filename')

    init_logbook(log_level, log_filename)
