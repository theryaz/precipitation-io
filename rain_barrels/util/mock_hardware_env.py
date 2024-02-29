from unittest.mock import MagicMock

def get_mock_hardware_environment():
    """
    Returns a dictionary of the mock hardware modules
    """
    pump = MagicMock()
    sensor = MagicMock()
    sensor.get_measurement.return_value = 100
    return {
        "pump": pump,
        "ultrasonic_sensor_device": sensor,
    }
