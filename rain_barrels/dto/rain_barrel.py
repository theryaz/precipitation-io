from dataclasses import dataclass
from math import pi


@dataclass
class RainBarrel:
    diameter: float
    """
    The diameter of the rain barrel in cm
    """
    height: float
    """
    The height of the rain barrel in cm
    """

    @property
    def radius(self) -> float:
        return self.diameter / 2

    @property
    def total_volume(self) -> float:
        """
        Returns the volume of the rain barrel in cubic cm
        """
        return self._volume(self.height)

    @property
    def volume_litres(self) -> float:
        """
        Returns the volume of the rain barrel in litres
        """
        return self.total_volume / 1000

    def compute_volume_full(self, water_level_cm: float) -> float:
        """
        Returns the volume of the rain barrel in litres given the level of the water
        """
        if water_level_cm > self.height:
            raise ValueError(
                f"The measurement given is greater than the height of the rain barrel {water_level_cm}cm > height: {self.height}cm"
            )
        return self._volume(max(water_level_cm, 0))

    def _volume(self, height) -> float:
        """
        Returns the volume of the rain barrel in cubic cm
        """
        return pi * height * (self.radius**2)
