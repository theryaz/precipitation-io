from unittest import TestCase

from rain_barrels.dto.reservoir import Reservoir
from rain_barrels.dto.rain_barrel import RainBarrel
from rain_barrels.dto.distance_sensor import DistanceSensor


class Testreservoir(TestCase):
    def setUp(self) -> None:
        self.rain_barrel1 = RainBarrel(
            diameter=55,
            height=95,
        )
        self.rain_barrel2 = RainBarrel(
            diameter=55,
            height=95,
        )
        self.reservoir = Reservoir(
            distance_sensor=DistanceSensor(dead_zone_cm=10, offset_cm=10),
            rain_barrels=[self.rain_barrel1, self.rain_barrel2]
        )
        return super().setUp()

    def test_volume(self):
        self.assertAlmostEqual(
            self.reservoir.total_volume,
            self.rain_barrel1.total_volume + self.rain_barrel2.total_volume,
            1,
        )

    def test_volume_litres(self):
        self.assertAlmostEqual(self.reservoir.total_volume_litres, 451.4, 1)

    def test_current_volume_litres_full(self):
        self.reservoir.set_volume_by_measurement(10)
        self.assertAlmostEqual(self.reservoir.current_volume_litres, 451.4, 1)

    def test_current_volume_litres_high(self):
        self.reservoir.set_volume_by_measurement(18)
        self.assertAlmostEqual(self.reservoir.current_volume_litres, 413.39, 1)

    def test_current_volume_litres_low(self):
        self.reservoir.set_volume_by_measurement(66)
        self.assertAlmostEqual(self.reservoir.current_volume_litres, 185.31, 1)

    def test_current_volume_litres_empty(self):
        self.reservoir.set_volume_by_measurement(105)
        self.assertAlmostEqual(self.reservoir.current_volume_litres, 0, 1)
