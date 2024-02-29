from drivers.ultrasonic_sensor_dev import UltrasonicSensorDevice

class VolumeSensor:
    def __init__(self, sensor: UltrasonicSensorDevice, offset_cm: float, dead_zone_cm: float):
        self.sensor = sensor
        self.offset_cm = offset_cm
        self.dead_zone_cm = dead_zone_cm

    offset_cm: float
    """
    The distance from the highest water level in centimeters
    """

    dead_zone_cm: float
    """
    The minimum distance the sensor can read accurately. Lower distances than this should be ignored.
    """

    def measure(self) -> int:
        return self.sensor.get_measurement()
