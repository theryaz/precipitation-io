from threading import Thread
from time import sleep

class PluginExample:
    _tick_thread: Thread = None
    _tick_thread_stop: bool = False

    def __init__(self, config: dict, resevoir, logger):
        print(f"PluginExample loaded with config: {config}")
        self.config = config or {}
        self.resevoir = resevoir
        self.logger = logger

    def start(self):
        if self._tick_thread is None:
            self._tick_thread_stop = False
            self_tick_thread = Thread(target=self._tick)
            self_tick_thread.start()

    def stop(self):
        if self._tick_thread is not None:
            self._tick_thread_stop = True
            self._tick_thread.join()
            self._tick_thread = None

    def _tick(self):
        while not self._tick_thread_stop:
            sleep(self.config.get("polling_rate", 1))
            print(self.resevoir.print_status)
