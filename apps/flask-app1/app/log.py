import logging, os
from os import environ

log_level = environ.get('LOG_LEVEL').upper()
log_dir = "logs"
log_file = "flask.log"

if not os.path.exists(log_dir):
        os.mkdir(log_dir)

logging.basicConfig(filename=log_dir + "/" + log_file, level=log_level)