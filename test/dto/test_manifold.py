from unittest import TestCase

from rain_barrels.dto.manifold import Manifold
from rain_barrels.dto.rain_barrel import RainBarrel


class TestManifold(TestCase):
    def setUp(self) -> None:
        self.rain_barrel1 = RainBarrel(
            diameter=36,
            height=24,
        )
        self.rain_barrel2 = RainBarrel(
            diameter=36,
            height=24,
        )
        self.manifold = Manifold(
            rain_barrels=[self.rain_barrel1, self.rain_barrel2], percent_full=50
        )
        return super().setUp()

    def test_volume(self):
        self.assertAlmostEqual(
            self.manifold.volume,
            self.rain_barrel1.volume + self.rain_barrel2.volume,
            1,
        )

    def test_volume_litres(self):
        self.assertAlmostEqual(self.manifold.total_volume_litres, 48.85, 1)

    def test_available_water_litres_full(self):
        self.manifold.percent_full = 100
        self.assertAlmostEqual(self.manifold.available_water_litres, 48.85, 1)

    def test_available_water_high(self):
        self.manifold.percent_full = 88
        self.assertAlmostEqual(self.manifold.available_water_litres, 42.99, 1)

    def test_available_water_low(self):
        self.manifold.percent_full = 23
        self.assertAlmostEqual(self.manifold.available_water_litres, 11.23, 1)

    def test_available_water_empty(self):
        self.manifold.percent_full = 0
        self.assertAlmostEqual(self.manifold.available_water_litres, 0, 1)
