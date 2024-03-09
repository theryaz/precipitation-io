import os
import importlib.util
from importlib import import_module
from rain_barrels.util.logger import LOGGER
from rain_barrels.models.resevoir import Resevoir


def load_plugins(resevoir: Resevoir, plugin_config: dict, logger, exclude=None):
    """
    Load all plugins in the rain_barrels/plugins directory
    """
    LOGGER.info("Loading plugins...")
    plugin_dir = os.path.join(os.path.dirname(__file__), "../..", "plugins")
    for file in os.listdir(plugin_dir):
        plugin_path = os.path.join(plugin_dir, file)
        config = plugin_config.get(file, { "enabled": False })
        if not (
            os.path.isdir(plugin_path)
            and not file.startswith("__")
        ):
            # Not a loadable plugin
            continue

        if not config.get("enabled", False):
            LOGGER.info(f"Plugin {file} is disabled")
            continue
    
        LOGGER.debug(f"Loading plugin: {file}")
        plugin = import_module(f"plugins.{file}")
        plugin.register(resevoir, config, logger)
