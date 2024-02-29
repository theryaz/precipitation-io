from random import randint
from time import sleep, time

import RPi.GPIO as GPIO
from rain_barrels.util.logger import LOGGER

from rain_barrels.util.is_raspberry_pi_env import is_raspberry_pi_env

HAS_REAL_HARDWARE = is_raspberry_pi_env()


class SwitchDevice:
    """
    Methods to be implemented on a GPIO device which can be simply switched on and off. pumps, lights, buzzers, etc.
    """

    def __init__(self, name: str, pin: int):
        self.name = name
        self.pin = pin

    def turn_on(self):
        raise NotImplementedError()

    def turn_off(self):
        raise NotImplementedError()
