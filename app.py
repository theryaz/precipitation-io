import os
import sys
from rain_barrels.util.use_hardware import is_raspberry_pi_env
from rain_barrels.util.load_irrigation_config import load_irrigation_system_config_from_file
from rain_barrels.util.logger import LOGGER

irrigation_system = None
plugin_config = None

def main():
    global irrigation_system
    global plugin_config
    file_path = os.getenv("CONFIG_FILE", "./config.json")
    mock_hardware = os.getenv("MOCK") == "true" or not is_raspberry_pi_env()
    irrigation_system, plugin_config = load_irrigation_system_config_from_file(file_path=file_path, use_mock_env=mock_hardware)

main()

print(irrigation_system.print_status)
from rain_barrels.util.load_plugins import load_plugins
load_plugins(irrigation_system, plugin_config, LOGGER)

msg = input("Press enter to quit")