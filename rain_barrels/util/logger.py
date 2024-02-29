# basic logger which writes to console and file

import logging
import os
import sys

from rain_barrels.config import LOG_DIR, LOG_FILE

# create the log directory if it doesn't exist
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# create a logger
LOGGER = logging.getLogger('rain_barrels')
LOGGER.setLevel(logging.DEBUG)

# create a file handler and set level to debug
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.DEBUG)

# create a console handler and set level to info
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

LOGGER.addHandler(file_handler)
LOGGER.addHandler(console_handler)