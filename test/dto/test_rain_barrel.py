from unittest import TestCase

from rain_barrels.dto.rain_barrel import RainBarrel


class TestRainBarrel(TestCase):
    def setUp(self) -> None:
        self.rain_barrel = RainBarrel(
            diameter=36,
            height=24,
        )
        return super().setUp()

    def test_volume(self):
        self.assertAlmostEqual(self.rain_barrel.volume, 24429.02, 1)

    def test_volume_litres(self):
        self.assertAlmostEqual(self.rain_barrel.volume_litres(), 24.4, 1)
