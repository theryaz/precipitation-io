from rain_barrels.drivers import Lcd
from threading import Thread
from time import sleep
from datetime import datetime


class _LCDDisplay():
    _thread: Thread = None
    _thread_stop: bool = False

    display = Lcd()
    
    display_text: list[str,str] = ["Hello World!", "I am a display!"]
    
    def _default_text(self):
        return ["Hello World!", self._current_time()]
    
    def _write(self, display_text: list[str,str] = None):
        '''
        Write to the display, only 16 chars and two lines
        '''
        if display_text is None:
            self._display_text = self._default_text()
        else:
            self._display_text = display_text
        self.display.lcd_display_string(self.display_text[0], 1)
        self.display.lcd_display_string(self.display_text[1], 2)
    
    def _current_time(self):
        now = datetime.now()
        return now.strftime("%H:%M:%S")
    
    def _run(self):
        while not self._thread_stop:
            self._write()
            sleep(1)
    
    def start(self):
        if self._thread is None:
            print("Starting LCD Display...")
            self._thread_stop = False
            self._thread = Thread(target=self._run)
            self._thread.start()

    def stop(self):
        if self._thread is not None:
            print("Stopping LCD Display...")
            self._thread_stop = True
            self._thread.join()
            self.display.lcd_clear()
            self._thread = None
            
LCDDisplay = _LCDDisplay()
"""
Singleton instance of the LCD Display.
"""