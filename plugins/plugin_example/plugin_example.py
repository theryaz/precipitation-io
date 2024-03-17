from threading import Thread
from time import sleep
from ..plugin import Plugin

class PluginExample(Plugin):
    
    def __init__(self, config: dict, resevoir, logger):
        super().__init__(config, resevoir, logger)
        print(f"PluginExample loaded with config: {config}")

    def _run(self):
        while not self.should_stop:
            sleep(self.config.get("polling_rate", 1))
            print(self.resevoir.print_status)