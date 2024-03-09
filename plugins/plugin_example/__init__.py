from .plugin_example import PluginExample

def register(resevoir, config, logger):
    PluginExample(config, resevoir, logger).start()
