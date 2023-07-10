from dataclasses import dataclass

from rain_barrels.dto.rain_barrel import RainBarrel


@dataclass
class Manifold:
    rain_barrels: list[RainBarrel]
    percent_full: int = 0

    full_distance_cm: float = 0
    empty_distance_cm: float = None

    def __post_init__(self):
        if self.empty_distance_cm is None:
            self.empty_distance_cm = self.rain_barrels[0].height

    @property
    def volume(self):
        """
        The total available volume of the manifold in cubic cm
        """
        return sum([rain_barrel.volume for rain_barrel in self.rain_barrels])

    @property
    def volume_litres(self):
        return self.volume / 1000

    @property
    def available_water_litres(self):
        return self.volume_litres * self.percent_full / 100

    @property
    def height(self):
        return self.rain_barrels[0].height

    @property
    def print_status(self):
        return f"Manifold Status: {self.percent_full}% full ({self.available_water_litres}L available)"

    def set_volume_by_measurement(self, measurement_cm: float, offset: int = 0):
        volume_full = self.compute_volume_full(measurement_cm - offset)
        self.percent_full = (volume_full / self.volume) * 100

    def compute_volume_full(self, measurement_cm: float):
        return sum(
            [
                rain_barrel.compute_volume_full(measurement_cm)
                for rain_barrel in self.rain_barrels
            ]
        )
