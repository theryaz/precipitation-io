import RPi.GPIO as GPIO
from time import sleep, time
from random import randint
from rain_barrels.util.logger import LOGGER

from rain_barrels.util.use_hardware import is_raspberry_pi_env

HAS_REAL_HARDWARE = is_raspberry_pi_env()


class UltrasonicSensorDevice:
    def __init__(self, name: str, trig_pin: int, echo_pin: int, debug: bool = False):
        self.name = name
        self._trig_pin = trig_pin
        self._echo_pin = echo_pin
        self._debug = debug
        self._setup_gpio_pins()

    def _debug_log(self, *args, **kwargs):
        if self._debug:
            LOGGER.debug(*args, **kwargs)

    def _setup_gpio_pins(self):
        """
        Sets GPIO to board mode, sets the TRIG and ECHO pins, and sets TRIG to output 0
        """
        GPIO.setup(self._trig_pin, GPIO.OUT)
        GPIO.setup(self._echo_pin, GPIO.IN)
        GPIO.output(self._trig_pin, 0)
        GPIO.setup(self._echo_pin, 0)

    def get_measurement(self) -> float:
        """
        Take a single measurement from the ultrasonic sensor. Returns distance in cm.
        """
        self._debug_log(
            f"[{self.name} UltrasonicSensorDevice] getting measurement {HAS_REAL_HARDWARE}",
        )

        # Send 20us pulse to trigger
        self._debug_log(f"[{self.name} UltrasonicSensorDevice] Sending Pulse")
        GPIO.output(self._trig_pin, GPIO.HIGH)
        sleep(0.00002)
        GPIO.output(self._trig_pin, GPIO.LOW)

        self._debug_log(
            f"[{self.name} UltrasonicSensorDevice] Waiting for echo to go high"
        )
        # Wait for echo to go high
        while GPIO.input(self._echo_pin) == GPIO.LOW:
            pass
        # Set the time, and wait for echo to go low
        self._debug_log(
            f"[{self.name} UltrasonicSensorDevice] Waiting for echo to go low"
        )
        start = time()
        while GPIO.input(self._echo_pin) == GPIO.HIGH:
            pass
        # Stop the time once we get the echo back
        stop = time()

        # Calculate the distance in cm
        # Speed of sound is 343 m/s, or 34300 cm/s
        # Half the distance is 343 / 2 = 171.5 * the time it took
        distance_cm = (stop - start) * 17150
        self._debug_log(
            f"[{self.name} UltrasonicSensorDevice] Returning result: {distance_cm}"
        )
        return distance_cm
