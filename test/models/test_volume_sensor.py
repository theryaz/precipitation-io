import test.util.hardware_mock
from unittest import TestCase
from unittest.mock import Mock
from rain_barrels.models.volume_sensor import VolumeSensor

class TestVolumeSensor(TestCase):

	def test_returns_the_measurement(self):
		mock_sensor = Mock(get_measurement=Mock(return_value=100.25))
		vs = VolumeSensor(mock_sensor, offset_cm=10, dead_zone_cm=30)

		self.assertAlmostEqual(vs.measure(), 90.25)

	def test_below_deadzone_is_zero(self):
		mock_sensor = Mock(get_measurement=Mock(return_value=35))
		vs = VolumeSensor(mock_sensor, offset_cm=10, dead_zone_cm=30)

		self.assertAlmostEqual(vs.measure(), 0)