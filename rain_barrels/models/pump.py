from rain_barrels.drivers.switch_device import SwitchDevice


class Pump:
    name: str

    def __init__(self, name: str, pump: SwitchDevice):
        self.name = name
        self._pump = pump

    def turn_on(self):
        self._pump.turn_on()

    def turn_off(self):
        self._pump.turn_off()
