import test.util.hardware_mock
from unittest import TestCase
from unittest.mock import Mock
from rain_barrels.models.pump import Pump

class TestPump(TestCase):

	def test_turns_the_pump_on(self):
		mock_switch = Mock()
		pump = Pump("test pump", mock_switch)

		pump.turn_on()

		mock_switch.turn_on.assert_called_once()

	def test_turns_the_pump_off(self):
		mock_switch = Mock()
		pump = Pump("test pump", mock_switch)

		pump.turn_off()

		mock_switch.turn_off.assert_called_once()