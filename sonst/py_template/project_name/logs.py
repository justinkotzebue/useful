from workflow_tools.logs import get_session_logger


def set_cli_logger(debug=False):
    get_session_logger(
        name='cloud_masking',
        set_exception_handler=True,
        level=('DEBUG' if debug else 'INFO'))
