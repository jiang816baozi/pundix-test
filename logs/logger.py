# logs/logger.py

import logging

def setup_logger(name, log_file, level=logging.DEBUG):
    handler = logging.FileHandler(log_file)
    handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
