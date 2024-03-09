import os
import importlib.util
from importlib import import_module
from rain_barrels.util.logger import LOGGER
from rain_barrels.models.resevoir import Resevoir


def load_plugins(resevoir: Resevoir, logger, exclude=None):
    """
    Load all plugins in the rain_barrels/plugins directory
    """
    exclude = ["plugin_example"] if exclude is None else exclude
    plugin_dir = os.path.join(os.path.dirname(__file__), "../..", "plugins")
    for file in os.listdir(plugin_dir):
        plugin_path = os.path.join(plugin_dir, file)
        if (
            file not in exclude
            and os.path.isdir(plugin_path)
            and not file.startswith("__")
        ):
            LOGGER.debug(f"Loading plugin: {file}")
            plugin = import_module(f"plugins.{file}")
            plugin.register(resevoir, logger)
