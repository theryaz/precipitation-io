from rain_barrels.util.logger import LOGGER

from rain_barrels.util.use_hardware import GPIO

class SwitchDevice:
    """
    Methods to be implemented on a GPIO device which can be simply switched on and off. pumps, lights, buzzers, etc.
    """

    def __init__(self, name: str, pin: int):
        self.name = name
        self.pin = pin
        
    def _setup_gpio_pins(self):
        self._pin_state = False
        self.turn_off()
        
    @property
    def pin_state(self):
        return self._pin_state
    
    def turn_on(self):
        LOGGER.debug(f"[SwitchDevice {self.name}] turn_on pin ${self.pin}")
        GPIO.output(self.pin, True)
        self._pin_state = True

    def turn_off(self):
        LOGGER.debug(f"[SwitchDevice {self.name}] turn_off pin ${self.pin}")
        GPIO.output(self.pin, False)
        self._pin_state = False
