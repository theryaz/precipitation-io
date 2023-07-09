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
        return pi * self.height * (self.radius**2)

    def volume_litres(self) -> float:
        """
        Returns the volume of the rain barrel in litres
        """
        return self.volume / 1000
