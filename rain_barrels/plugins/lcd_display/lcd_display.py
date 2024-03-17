from datetime import datetime
from time import sleep
from ..plugin import Plugin
from rain_barrels.util.use_hardware import is_raspberry_pi_env
from rain_barrels.drivers.i2c_dev import Lcd

class MockDisplay():
    def lcd_display_string(self, text, line):
        print(f"[{line}] {text}")

class LCDDisplay(Plugin):
    
    display = None
    _display_text: list[str, str] = ["Hello World!", "I am a display!"]
    
    def __init__(self, config: dict, irrigation_system, logger):
        super().__init__(config, irrigation_system, logger)
        if is_raspberry_pi_env():
            self.display = Lcd()
        else:
            self.logger.debug("[LCDDisplay] Running in mock environment. Printing display to console")
            self.display = MockDisplay()
        self._refresh_rate = config.get("refresh_rate", 1)
        
    def _run(self):
        while not self.should_stop:
            self._refresh_display_status()
            self._write()
            sleep(self._refresh_rate)
            
    def _refresh_display_status(self):
        percent_full = self.irrigation_system.percent_full
        self._display_text[0] = f"Water Level: {percent_full}%"
        if self.irrigation_system.pump_is_on:
            self._display_text[1] = "Pump: ON"
        self._display_text[1] = f"{self._current_time()}"
        
    def _current_time(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S")
    
    def _default_text(self):
        return ["Hello World!", self._current_time()]
    
    def _write(self):
        """
        Write to the display, only 16 chars and two lines
        """
        self.display.lcd_display_string(self._display_text[0][:16], 1)
        self.display.lcd_display_string(self._display_text[1][:16], 2)
