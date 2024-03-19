import rain_barrels.util.use_hardware
from unittest import TestCase
from unittest.mock import MagicMock, patch, call
from parameterized import parameterized
from rain_barrels.models.irrigation_system import IrrigationSystem
from rain_barrels.models.volume_sensor import VolumeSensor
from rain_barrels.models.tank import Tank
from rain_barrels.models.pump import Pump
from rain_barrels.drivers.ultrasonic_sensor_dev import UltrasonicSensorDevice
from rain_barrels.drivers.switch_device import SwitchDevice


class TestIrrigationSystem(TestCase):

    def setUp(self) -> None:
        self.mock_gpio = patch(
            "rain_barrels.drivers.ultrasonic_sensor_dev.GPIO"
        ).start()
        self.mock_gpio.LOW = 0
        self.mock_gpio.HIGH = 1

        self.switch_gpio = patch(
            "rain_barrels.drivers.switch_device.GPIO", self.mock_gpio
        ).start()

    def tearDown(self) -> None:
        patch.stopall()

    def _setup_irrigation_system(self, trig_pin, echo_pin, pump_pin, pct_full: int):
        sensor_dev = UltrasonicSensorDevice(
            name="Mock Ultrasonic Sensor", trig_pin=trig_pin, echo_pin=echo_pin
        )
        volume_sensor = VolumeSensor(offset_cm=5, dead_zone_cm=30, sensor=sensor_dev)
        pump_switch_dev = SwitchDevice(name="Mock Pump Switch", pin=pump_pin)
        pump = Pump("My pump", pump_switch_dev)
        tanks = [
            Tank("tank1", 60, 125),
            Tank("tank2", 60, 125),
        ]
        irrigation_system = IrrigationSystem(
            name="Test irrigation_system",
            volume_sensor=volume_sensor,
            pump=pump,
            tanks=tanks,
        )
        self._mock_measured_volume_result(
            irrigation_system.height + volume_sensor.offset_cm, pct_full
        )
        return irrigation_system

    def _mock_measured_volume_result(self, height_cm: int, pct_full: int):
        target_measured_height = height_cm - (height_cm * (pct_full / 100))
        measured_time = target_measured_height / 17150
        mock_time = patch("rain_barrels.drivers.ultrasonic_sensor_dev.time").start()
        mock_time.side_effect = [0, measured_time]
        return mock_time

    def assertGPIOInputCalledWith(self, pin: int):
        self.mock_gpio.input.assert_called_with(pin)

    def assertGPIOOutputCalledWith(self, pin: int, high_or_low):
        self.mock_gpio.output.assert_has_calls(calls=[call(pin, high_or_low)])

    def assertUltrasonicSensorPulseSent(self, trig, echo):
        self.mock_gpio.output.assert_has_calls(
            calls=[
                call(trig, 1),
                call(trig, 0),
            ]
        )
        self.assertGPIOInputCalledWith(echo)

    def test_calculates_capacity_from_configuration(self):
        sut = self._setup_irrigation_system(1, 2, 3, pct_full=50)

        total_capacity_litres = sut.total_capacity_litres

        self.assertAlmostEqual(total_capacity_litres, 706.85834705)

    def test_pump_is_turned_on(self):
        sut = self._setup_irrigation_system(1, 2, 3, pct_full=50)

        sut.turn_pump_on()

        self.assertTrue(sut.pump_is_on)
        self.assertGPIOOutputCalledWith(3, 0)

    def test_pump_is_turned_off(self):
        sut = self._setup_irrigation_system(1, 2, 3, pct_full=50)

        sut.turn_pump_off()

        self.assertFalse(sut.pump_is_on)
        self.assertGPIOOutputCalledWith(3, 0)

    def test_pump_toggle_turns_pump_on_and_off(self):
        sut = self._setup_irrigation_system(1, 2, 3, pct_full=50)

        sut.toggle_pump()
        self.assertTrue(sut.pump_is_on)
        sut.toggle_pump()

        self.assertFalse(sut.pump_is_on)
        self.assertGPIOOutputCalledWith(3, 1)
        self.assertGPIOOutputCalledWith(3, 0)

    @parameterized.expand(
        [
            (10, 73.513),
            (25, 183.783),
            (55, 404.323),
            (75, 706.858),
            (90, 706.858),
            (100, 706.858),
        ]
    )
    def test_calculates_current_volume(self, pct_full, expected_volume_litres):
        """
        Beyond sensor deadzone, readings default to 100% full
        """
        sut = self._setup_irrigation_system(1, 2, 3, pct_full=pct_full)

        current_volume_litres = sut.current_volume_litres

        self.assertAlmostEqual(current_volume_litres, expected_volume_litres, 3)
        self.assertUltrasonicSensorPulseSent(1, 2)
