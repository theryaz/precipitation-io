import json
from rain_barrels.util.logger import LOGGER
from rain_barrels.models.pump import Pump
from rain_barrels.models.resevoir import Resevoir
from rain_barrels.models.tank import Tank
from rain_barrels.models.volume_sensor import VolumeSensor
from rain_barrels.util.use_hardware import get_mock_hardware_environment
from rain_barrels.drivers.ultrasonic_sensor_dev import UltrasonicSensorDevice
from rain_barrels.drivers.switch_device import SwitchDevice

def _default_mock_resevoir():
	mock_env = get_mock_hardware_environment()
	return (Resevoir(
			name="Default Mock Resevoir",
			volume_sensor=VolumeSensor(offset_cm=5,
																dead_zone_cm=30,
																sensor=mock_env["ultrasonic_sensor_device"]),
			pump=Pump("Pump", mock_env["pump"]),
			tanks=[Tank("tank1", 35, 120), Tank("tank2", 35, 120)]
	), {})

def load_resevoir_config_from_file(file_path="./resevoir.config.json", use_mock_env: bool = True) -> Resevoir:
		resevoir_config = None
		try:
			with open(file_path, "r") as f:
					resevoir_config = json.load(f)
		except Exception as e:
			LOGGER.error(f"Error loading resevoir config: {e}")
			LOGGER.info(f"Using mock resevoir: {e}")
			return _default_mock_resevoir()

		try:
			ultrasonic_sensor_device = None
			pump_switch = None
			if use_mock_env:
				mock_env = get_mock_hardware_environment()
				ultrasonic_sensor_device = mock_env["ultrasonic_sensor_device"]
				pump_switch = mock_env["pump"]
			else:
				ultrasonic_sensor_device = UltrasonicSensorDevice(
						name="Volume Sensor",
						trig_pin=resevoir_config["ultrasonic_sensor"]["trigger_pin"],
						echo_pin=resevoir_config["ultrasonic_sensor"]["echo_pin"],
						debug=resevoir_config["ultrasonic_sensor"].get("debug", False)
				)
				pump_switch = SwitchDevice(
						name="Pump",
						pin=resevoir_config["pump_switch"]["pin"]
				)

			return (Resevoir(
					name=resevoir_config["name"],
					volume_sensor=VolumeSensor(offset_cm=resevoir_config["ultrasonic_sensor"]["offset_cm"],
																			dead_zone_cm=resevoir_config["ultrasonic_sensor"]["dead_zone_cm"],
																			sensor=ultrasonic_sensor_device),
					pump=Pump("Pump", pump_switch),
					tanks=[Tank(tank.get("name", ""), tank["diameter_cm"], tank["height_cm"]) for tank in resevoir_config["tanks"]]
			), resevoir_config["plugins"])
		except KeyError as e:
			LOGGER.error(f"KeyError loading resevoir config. Refer to example-resevoir.config.json for expected values.")
			LOGGER.error(e)
			raise e