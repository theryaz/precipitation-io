import test.util.hardware_mock
from unittest import TestCase
from rain_barrels.models.tank import Tank

class TestTank(TestCase):

	def test_calculates_capacity(self):
		tank = Tank("test", 60, 125)
		self.assertAlmostEqual(tank.capacity_litres, 353.429, 3)

	def test_calculates_volume_full(self):
		tank = Tank("test", 60, 125)
		pct = 70 / 125
		self.assertAlmostEqual(tank.compute_volume_full(70), tank.capacity_litres * pct)
