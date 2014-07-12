"""
initialize logger
"""
from logging import StreamHandler, Formatter, FileHandler, getLogger, DEBUG, ERROR
import os.path


def initialize_logger(output_dir):
    """
    copied from
    http://aykutakin.wordpress.com/2013/08/06/logging-to-console-and-file-in-python/
    """
    logger = getLogger()
    logger.setLevel(DEBUG)

    # create console handler and set level to info
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    formatter = Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create error file handler and set level to error
    handler = FileHandler(os.path.join(output_dir, "error.log"),
                          "w",
                          encoding=None,
                          delay="true")
    handler.setLevel(ERROR)
    formatter = Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create debug file handler and set level to debug
    handler = FileHandler(os.path.join(output_dir, "all.log"), "w")
    handler.setLevel(ERROR)
    formatter = Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def initialize_logger_console():
    """
    copied from
    http://aykutakin.wordpress.com/2013/08/06/logging-to-console-and-file-in-python/
    """
    logger = getLogger()
    logger.setLevel(DEBUG)

    # create console handler and set level to info
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    formatter = Formatter("%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)