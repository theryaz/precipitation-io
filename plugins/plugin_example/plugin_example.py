from time import sleep
from ..plugin import Plugin

class PluginExample(Plugin):
    
    def __init__(self, config: dict, irrigation_system, logger):
        super().__init__(config, irrigation_system, logger)
        print(f"PluginExample loaded with config: {config}")

    def _run(self):
        while not self.should_stop:
            sleep(self.config.get("polling_rate", 1))
            print(self.irrigation_system.print_status)