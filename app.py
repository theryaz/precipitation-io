from rain_barrels.util.is_raspberry_pi_env import is_raspberry_pi_env
from rain_barrels.util.mock_hardware_modules import mock_hardware_modules
from rain_barrels.util.logger import LOGGER

if not is_raspberry_pi_env():
    mock_hardware_modules()

from rain_barrels.util.mock_hardware_env import get_mock_hardware_environment
import RPi.GPIO as GPIO

from rain_barrels.models.pump import Pump
from rain_barrels.models.resevoir import Resevoir
from rain_barrels.models.tank import Tank
from rain_barrels.models.volume_sensor import VolumeSensor

mock_env = get_mock_hardware_environment()

resevoir = Resevoir(
    name="Ryan's Resevoir",
    volume_sensor=VolumeSensor(offset_cm=5,
                               dead_zone_cm=30,
                               sensor=mock_env["ultrasonic_sensor_device"]),
    pump=Pump("Pump", mock_env["pump"]),
    tanks=[Tank(35, 120), Tank(35, 120)]
)



print(resevoir.print_status)
from rain_barrels.util.load_plugins import load_plugins
load_plugins(resevoir, LOGGER)