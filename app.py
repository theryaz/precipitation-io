import os
import sys
from rain_barrels.util.use_hardware import is_raspberry_pi_env
from rain_barrels.util.load_resevoir_config import load_resevoir_config_from_file
from rain_barrels.util.logger import LOGGER

resevoir = None
plugin_config = None

def main():
    global resevoir
    global plugin_config
    file_path = os.getenv("CONFIG_FILE", "./resevoir.config.json")
    mock_hardware = os.getenv("MOCK") == "true" or not is_raspberry_pi_env()
    resevoir, plugin_config = load_resevoir_config_from_file(file_path=file_path, use_mock_env=mock_hardware)

main()

print(resevoir.print_status)
from rain_barrels.util.load_plugins import load_plugins
load_plugins(resevoir, plugin_config, LOGGER)

msg = input("Press enter to quit")