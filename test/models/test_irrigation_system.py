import test.util.hardware_mock
from unittest import TestCase
from unittest.mock import Mock
from rain_barrels.models.irrigation_system import IrrigationSystem
from rain_barrels.models.volume_sensor import VolumeSensor
from rain_barrels.models.tank import Tank
from rain_barrels.models.pump import Pump

class TestIrrigationSystem(TestCase):

	def setUp(self) -> None:
		self.mock_volume_sensor = Mock()
		self.mock_switch = Mock()
		self.pump = Pump("My pump", self.mock_switch)
		self.tanks = [
			Tank("tank1" , 60, 125),
			Tank("tank2", 60, 125),
		]

	def test_calculates_capacity(self):
		irrigation_system = IrrigationSystem(
			name="Test irrigation_system",
			volume_sensor=self.mock_volume_sensor,
			pump=self.pump,
			tanks=self.tanks,
		)
		self.assertAlmostEqual(irrigation_system.total_capacity_litres, self.tanks[0].capacity_litres * 2)

	def test_calculates_current_volume_low(self):
		irrigation_system = IrrigationSystem(
			name="Test irrigation_system",
			volume_sensor=self.mock_volume_sensor,
			pump=self.pump,
			tanks=self.tanks,
		)
		self.mock_volume_sensor.measure.return_value=100
		self.assertAlmostEqual(irrigation_system.current_volume_litres, 141.372, 3)

	def test_calculates_current_volume_med(self):
		irrigation_system = IrrigationSystem(
			name="Test irrigation_system",
			volume_sensor=self.mock_volume_sensor,
			pump=self.pump,
			tanks=self.tanks,
		)
		self.mock_volume_sensor.measure.return_value=55
		self.assertAlmostEqual(irrigation_system.current_volume_litres, 395.841, 3)

	def test_calculates_current_volume_high(self):
		irrigation_system = IrrigationSystem(
			name="Test irrigation_system",
			volume_sensor=self.mock_volume_sensor,
			pump=self.pump,
			tanks=self.tanks,
		)
		self.mock_volume_sensor.measure.return_value=5
		self.assertAlmostEqual(irrigation_system.current_volume_litres, 678.584, 3)
