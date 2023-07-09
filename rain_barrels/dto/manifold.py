from dataclasses import dataclass

from rain_barrels.dto.rain_barrel import RainBarrel


@dataclass
class Manifold:
    rain_barrels: list[RainBarrel]
    percent_full: int = 0

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
