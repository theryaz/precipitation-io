from .scheduler import Scheduler

def register(irrigation_system, config, logger):
    Scheduler(config, irrigation_system, logger).start()
