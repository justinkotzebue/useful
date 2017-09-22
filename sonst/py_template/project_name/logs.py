import logging
from dhi_mailer import handler
from workflow_tools.logs import get_session_logger


def set_cli_logger(logfile=None, debug=False):
    get_session_logger(
        name='cloud_masking',
        logfile=logfile,
        set_exception_handler=True,
        level=('DEBUG' if debug else 'INFO'))

    logger = logging.getLogger("cloud_masking")
    h= handler.EmailHandler(sender='juko@dhigroup.com', recipient="juko@dhigroup.com")
    h.setLevel=("ERROR")
    formatter = logging.Formatter('%(asctime)s %(name)s - %(message)s')
    h.setFormatter(formatter)
    logger.addHandler(h)
