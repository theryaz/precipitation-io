from threading import Thread
from ..plugin import Plugin
import rain_barrels.util.use_hardware
import RPi.GPIO as GPIO

class ButtonToggle(Plugin):
    
    def __init__(self, config: dict, resevoir, logger):
        super().__init__(config, resevoir, logger)
        self._setup_pins()
    
    def _setup_pins(self):
        self.pin = self.config["pin"]
        self.logger.debug(f"[ButtonToggle] Setting up button toggle on pin {self.pin}")
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self._button_pressed, bouncetime=200)
        
    def _button_pressed(self, channel):
        self.logger.debug(f"[ButtonToggle] Button pressed!")
        self.resevoir.toggle_pump()
