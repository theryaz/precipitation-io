from .plugin_example import PluginExample

def register(irrigation_system, config, logger):
    PluginExample(config, irrigation_system, logger).start()
