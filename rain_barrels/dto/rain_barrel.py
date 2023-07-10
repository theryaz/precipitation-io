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
    def volume(self) -> float:
        """
        Returns the volume of the rain barrel in cubic cm
        """
        return self._volume(self.height)

    @property
    def volume_litres(self) -> float:
        """
        Returns the volume of the rain barrel in litres
        """
        return self.volume / 1000

    def compute_volume_full(self, measurement_cm: float) -> float:
        """
        Returns the volume of the rain barrel in litres given the top level of the water
        """
        return self._volume(self.height) - self._volume(max(measurement_cm, 0))

    def _volume(self, height) -> float:
        """
        Returns the volume of the rain barrel in cubic cm
        """
        return pi * self.height * (self.radius**2)
