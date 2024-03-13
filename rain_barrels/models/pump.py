from rain_barrels.drivers.switch_device import SwitchDevice


class Pump:
    name: str

    def __init__(self, name: str, switch: SwitchDevice):
        self.name = name
        self._pump = switch
    
    @property
    def is_on(self):
        return self._pump.pin_state

    def turn_on(self):
        self._pump.turn_on()

    def turn_off(self):
        self._pump.turn_off()
