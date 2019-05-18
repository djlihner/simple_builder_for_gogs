import logging
from flask.logging import default_handler

formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(message)s")

default_handler.setFormatter(formatter)
logging.getLogger('werkzeug').addHandler(default_handler)


def get_logger():
    return logging.getLogger('werkzeug')
