from dataclasses import dataclass

from rain_barrels.dto.distance_sensor import DistanceSensor
from rain_barrels.dto.rain_barrel import RainBarrel


@dataclass
class Reservoir:
    """
    A reservoir is a collection of rain barrels that are connected together.
    """
    distance_sensor: DistanceSensor
    rain_barrels: list[RainBarrel]
    current_volume_litres: float = 0

    @property
    def total_volume(self):
        """
        The total available volume of the reservoir in cubic cm
        """
        return sum([rain_barrel.total_volume for rain_barrel in self.rain_barrels])

    @property
    def total_volume_litres(self):
        return self.total_volume / 1000

    @property
    def percent_full(self):
        return (self.current_volume_litres / self.total_volume_litres) * 100

    @property
    def height(self):
        return self.rain_barrels[0].height

    @property
    def print_status(self):
        return f"reservoir Status: {round(self.percent_full, 2)}% full ({round(self.current_volume_litres, 2)}/{round(self.total_volume_litres)} L)"

    @property
    def print_status_short(self):
        return f"{round(self.percent_full, 2)}% - {round(self.current_volume_litres, 2)}L"

    def set_volume_by_measurement(self, measurement_cm: float):
        water_level_cm = self.distance_sensor.get_water_level(
            measurement_cm, self.height
        )
        self.current_volume_litres = (
            sum(
                [
                    rain_barrel.compute_volume_full(water_level_cm)
                    for rain_barrel in self.rain_barrels
                ]
            )
            / 1000
        )
        return {
            "volume_litres": self.current_volume_litres,
            "percent_full": self.percent_full,
        }
