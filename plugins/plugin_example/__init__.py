from .plugin_example import PluginExample, PluginExampleConfig

def register(resevoir, logger):
    logger.debug("PluginTest registered")
    logger.debug(f"PluginTest resevoir: {resevoir.print_status_short}")
    config = PluginExampleConfig(polling_rate=1)
    PluginExample(config, resevoir, logger).start()
