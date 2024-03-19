from threading import Thread
from rain_barrels.models.irrigation_system import IrrigationSystem

class Plugin:
    _run_thread: Thread = None
    _run_thread_stop: bool = False

    def __init__(self, config: dict, irrigation_system: IrrigationSystem, logger):
        self.config = config or {}
        self.irrigation_system = irrigation_system
        self.logger = logger

    def start(self):
        if self._run_thread is None:
            self._run_thread_stop = False
            self_run_thread = Thread(target=self._run)
            self_run_thread.start()

    def stop(self):
        if self._run_thread is not None:
            self._run_thread_stop = True
            self._run_thread.join()
            self._run_thread = None
            
    @property
    def should_stop(self):
        return self._run_thread_stop
    
    def _run(self):
        pass

