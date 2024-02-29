from functools import lru_cache
from math import pi

class Tank:
    def __init__(
        self,
    ):
        pass

    diameter: float
    """
    The diameter of the rain barrel in cm
    """
    height: float
    """
    The height of the rain barrel in cm
    """

    _capacity_cm2: float = None

    @lru_cache
    def compute_volume_full(self, water_level_cm: float) -> float:
        """
        Returns the volume of the rain barrel in litres given the level of the water
        """
        if water_level_cm > self.height:
            raise ValueError(
                f"The measurement given is greater than the height of the rain barrel {water_level_cm}cm > height: {self.height}cm"
            )
        volume_cm = self._compute_capacity_cm2(max(water_level_cm, 0))
        return volume_cm / 1000  # Convert to litres

    @property
    def radius(self) -> float:
        return self.diameter / 2

    @property
    def capacity_litres(self) -> float:
        """
        Returns the volume of the rain barrel in litres
        """
        if not self._capacity_cm2:
            self.capacity_cm2 = self._compute_capacity_cm2(self.height)
        return self.capacity_cm2 / 1000

    def _compute_capacity_cm2(self, height: int) -> float:
        """
        Returns the volume of the rain barrel in cubic cm
        """
        return pi * height * (self.radius**2)
