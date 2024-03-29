from math import pi


class Tank:
    def __init__(self, name: str, diameter_cm: float, height_cm: float):
        self.name = name
        self.diameter_cm = diameter_cm
        self.height_cm = height_cm
        self._capacity_cm2 = self._compute_capacity_cm2(self.height_cm)

    diameter_cm: float
    """
    The diameter of the rain barrel in cm
    """
    height_cm: float
    """
    The height of the rain barrel in cm
    """

    _capacity_cm2: float = None

    def compute_volume_full(self, water_level_cm: float) -> float:
        """
        Returns the volume of the rain barrel in litres given the level of the water
        """
        if water_level_cm > self.height_cm:
            raise ValueError(
                f"The measurement given is greater than the height of the rain barrel {water_level_cm}cm > height: {self.height_cm}cm"
            )
        volume_cm = self._compute_capacity_cm2(max(water_level_cm, 0))
        return volume_cm / 1000  # Convert to litres

    @property
    def radius(self) -> float:
        return self.diameter_cm / 2

    @property
    def capacity_litres(self) -> float:
        """
        Returns the volume of the rain barrel in litres
        """
        return self._capacity_cm2 / 1000

    def _compute_capacity_cm2(self, height_cm: int) -> float:
        """
        Returns the volume of the rain barrel in cubic cm
        """
        return pi * height_cm * (self.radius**2)
