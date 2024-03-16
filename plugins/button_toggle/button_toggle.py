from threading import Thread
import rain_barrels.util.use_hardware
import RPi.GPIO as GPIO

class ButtonToggle:
    _tick_thread: Thread = None
    _tick_thread_stop: bool = False

    def __init__(self, config: dict, resevoir, logger):
        print(f"[ButtonToggle] loaded with config: {config}")
        self.config = config or {}
        self.resevoir = resevoir
        self.logger = logger
        self._setup_pins()
    
    def _setup_pins(self):
        self.pin = self.config["pin"]
        self.logger.debug(f"[ButtonToggle] Setting up button toggle on pin {self.pin}")
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self._button_pressed, bouncetime=200)

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
            pass
        
    def _button_pressed(self, channel):
        self.logger.debug(f"[ButtonToggle] Button pressed!")
        self.resevoir.toggle_pump()
