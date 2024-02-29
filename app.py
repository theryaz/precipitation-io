from rain_barrels.util.is_raspberry_pi_env import is_raspberry_pi_env
from rain_barrels.util.mock_hardware_modules import mock_hardware_modules

if not is_raspberry_pi_env():
    mock_hardware_modules()

import RPi.GPIO as GPIO

from rain_barrels.models import Pump, Resevoir, Tank, VolumeSensor

Resevoir = Resevoir("Ryan's mock", VolumeSensor("Mock Volume Sensor"), [Tank(), Tank()])
