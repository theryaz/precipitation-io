"""
Import hardware helpers from this file to automatically mock hardware modules if not running on a Raspberry Pi.
"""

from rain_barrels.util.is_raspberry_pi_env import is_raspberry_pi_env
from rain_barrels.util.mock_hardware_modules import mock_hardware_modules

mocked_modules = None
if not is_raspberry_pi_env():
    mocked_modules = mock_hardware_modules()

import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
