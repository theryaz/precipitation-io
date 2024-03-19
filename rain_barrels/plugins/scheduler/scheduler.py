import schedule
from time import sleep
from ..plugin import Plugin

class Scheduler(Plugin):
    
    def __init__(self, config: dict, irrigation_system, logger):
        super().__init__(config, irrigation_system, logger)
        self.logger.debug(f"[Scheduler] loaded with config: {config}")
        self._setup_scheduler()
        
    def _setup_scheduler(self):
        devmode_schedule = self.config.get("devmode_schedule", False)
        if devmode_schedule:
            self.logger.debug(f"[Scheduler] loaded running in devmode. Pump should run for 5 seconds every minute.")
            schedule.every(1).minutes.do(self._run_pump_for_seconds, 5)
        else:
            daily_run_time = self.config.get("daily_run_time", "07:30")
            seconds = self.config.get("daily_run_time_seconds", 60)
            schedule.every().day.at(daily_run_time).do(self._run_pump_for_seconds, seconds)
        

    def _run_pump_for_seconds(self, seconds: int):
        self.logger.info(f"[Scheduler] Running pump for {seconds} seconds")
        self.irrigation_system.turn_pump_on()
        sleep(seconds)
        self.irrigation_system.turn_pump_off()
        self.logger.info(f"[Scheduler] Stopping pump")

    def _run(self):
        while not self.should_stop:
            sleep(self.config.get("polling_rate", 1))
            schedule.run_pending()