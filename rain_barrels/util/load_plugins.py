import os
import importlib.util
from importlib import import_module
from rain_barrels.util.logger import LOGGER
from rain_barrels.models.irrigation_system import IrrigationSystem


def load_plugins(irrigation_system: IrrigationSystem, plugin_config: dict, logger, exclude=None):
    """
    Load all plugins in the rain_barrels/plugins directory
    """
    LOGGER.info("Loading plugins...")
    plugin_dir = os.path.join(os.path.dirname(__file__), "../", "plugins")
    for file in os.listdir(plugin_dir):
        plugin_path = os.path.join(plugin_dir, file)
        config = plugin_config.get(file, { "enabled": False })
        if not (
            os.path.isdir(plugin_path)
            and not file.startswith("__")
        ):
            # Not a loadable plugin
            continue

        if config.get("enabled", False):
            LOGGER.debug(f"Loading plugin: {file}")
            plugin = import_module(f"rain_barrels.plugins.{file}")
            plugin.register(irrigation_system, config, logger)
        else:
            LOGGER.info(f"Plugin {file} is disabled")
    
