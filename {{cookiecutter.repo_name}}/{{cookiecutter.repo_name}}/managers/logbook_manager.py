import logbook
import sys


def _get_logbook_logging_level(level_str):
    """
    return logbook level object from given string level
    """
    if level_str in ('CRITICAL', 'ERROR', 'WARNING', 'NOTICE',
                     'INFO', 'DEBUG', 'TRACE', 'NOTSET'):
        return getattr(logbook, level_str)
    else:
        raise ValueError("Unknown logbook log level: {}".format(level_str))


def init_logbook(log_level_str, filename):
    """
    initialize logbook
    """
    log_level_str = log_level_str.upper().strip()
    log_level = _get_logbook_logging_level(log_level_str)

    if not filename:
        logbook.StreamHandler(sys.stdout, level=log_level).push_application()
    else:
        logbook.TimedRotatingFileHandler(
            filename, level=log_level,
            date_format="%Y-%m-%d").push_application()

    msg = 'Logging initialized, level: {}, mode: {}'.format(
        log_level_str,
        "stdout mode" if not filename else 'file mode: ' + filename
    )

    # log startup message
    logbook.Logger('App').notice(msg)
