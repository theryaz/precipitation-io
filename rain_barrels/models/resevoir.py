from rain_barrels.util.logger import LOGGER
from .volume_sensor import VolumeSensor
from .tank import Tank
from .pump import Pump


class Resevoir:

    def __init__(
        self, name: str, volume_sensor: VolumeSensor, pump: Pump, tanks: list[Tank] = []
    ):
        self.name = name
        self.volume_sensor = volume_sensor
        self.pump = pump
        self.tanks = tanks

    name: str
    volume_sensor: VolumeSensor
    tanks: list[Tank]
    _current_volume_litres: int = 0

    def turn_pump_on(self):
        LOGGER.info("Pump turned on")
        self.pump.turn_on()

    def turn_pump_off(self):
        LOGGER.info("Pump turned off")
        self.pump.turn_off()

    @property
    def total_capacity_litres(self):
        """
        The total available capacity of the resevoir in litres
        """
        return sum([tank.capacity_litres for tank in self.tanks])

    @property
    def current_volume_litres(self):
        """
        The total available capacity of the resevoir in litres
        """
        self._measure_current_volume()
        return self._current_volume_litres

    @property
    def percent_full(self):
        return (self._current_volume_litres / self.total_capacity_litres) * 100

    @property
    def height(self):
        return self.tanks[0].height_cm

    @property
    def print_status(self):
        return f"{self.name} Resevoir Status: {round(self.percent_full, 2)}% full ({round(self.current_volume_litres, 2)}/{round(self.total_capacity_litres)} L)"

    @property
    def print_status_short(self):
        return (
            f"{round(self.percent_full, 2)}% - {round(self.current_volume_litres, 2)}L"
        )

    def _get_water_level(self) -> float:
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
        return self.height - max(0, self.volume_sensor.measure())

    def _measure_current_volume(self):
        water_level_cm = self._get_water_level()
        self._current_volume_litres = sum(
            [tank.compute_volume_full(water_level_cm) for tank in self.tanks]
        )
        return {
            "volume_litres": self._current_volume_litres,
            "percent_full": self.percent_full,
        }
