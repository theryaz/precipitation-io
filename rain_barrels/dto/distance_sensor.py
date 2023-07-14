from dataclasses import dataclass
from math import pi


@dataclass
class DistanceSensor:
    offset_cm: float
    """
    The distance from the highest water level in centimeters
    """

    dead_zone_cm: float
    """
    The minimum distance the sensor can read accurately. Lower distances than this should be ignored.
    """

    def get_water_level(self, distance_cm: float, height: float) -> float:
        """
        Returns the water level in centimeters
        _. <- Sensor
        |         |  |  |
        |         |  |  | <- Offset
        ++++++++  |  | <- Dead zone
        |      |  |  <- Distance
        |------| <- Water level
        |ssssss|
        ++++++++

        Given the height of the barrel, the distance from the sensor minus the offset is the waterlevel.

        The deadzone is factored in if the offset is less than the deadzone,
        the water should be considered full in this case since we can't get an accurate reading, but know it's close to full.

        """
        if distance_cm <= self.dead_zone_cm:
            return height  # Assume barrel is full
        return height - max(0, distance_cm - self.offset_cm)
