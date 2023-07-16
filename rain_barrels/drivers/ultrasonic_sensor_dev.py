import RPi.GPIO as GPIO
from time import sleep, time
from random import randint

from rain_barrels.util.is_raspberry_pi_env import is_raspberry_pi_env

HAS_REAL_HARDWARE = is_raspberry_pi_env()

class UltrasonicSensorDevice():
    def __init__(self, trig_pin: int, echo_pin: int):
        self._trig_pin = trig_pin
        self._echo_pin = echo_pin

    def _setup_gpio_pins(self):
        '''
        Sets GPIO to board mode, sets the TRIG and ECHO pins, and sets TRIG to output 0
        '''
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._trig_pin,GPIO.OUT)
        GPIO.setup(self._echo_pin, GPIO.IN)
        GPIO.output(self._trig_pin,0)

    def get_measurement(self) -> float:
        '''
        Take a single measurement from the ultrasonic sensor. Returns distance in cm.
        '''
        print(f"getting measurement {HAS_REAL_HARDWARE}")
        if not HAS_REAL_HARDWARE:
            print("RPi env not detected, mocking Ultrasonic Sensor result")
            return randint(25, 95)
            
        # Send 20us pulse to trigger
        GPIO.output(self._trig_pin, 1)
        sleep(0.00002)
        GPIO.output(self._trig_pin, 0)

        # Wait for echo to go high
        while GPIO.input(self._echo_pin) == 0:
            pass
        # Set the time, and wait for echo to go low
        start = time()
        while GPIO.input(self._echo_pin) == 1:
            pass
        # Stop the time once we get the echo back
        stop = time()

        # Calculate the distance in cm
        # Speed of sound is 343 m/s, or 34300 cm/s
        # Half the distance is 343 / 2 = 171.5 * the time it took
        return (stop - start) * 17150