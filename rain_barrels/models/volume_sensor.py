from rain_barrels.drivers.ultrasonic_sensor_dev import UltrasonicSensorDevice

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

    def measure(self) -> float:
        raw_distance = self.sensor.get_measurement()
        surface_distance = raw_distance - self.offset_cm
        if surface_distance <= self.dead_zone_cm:
            # Any measurement closer than the deadzone is unreliable so treat it as 0cm distance, or 100% full
            return 0
        return surface_distance
