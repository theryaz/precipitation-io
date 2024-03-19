from unittest.mock import MagicMock, Mock

def get_mock_hardware_environment():
    """
    Returns a dictionary of the mock hardware modules
    """
    switch = MagicMock()
    # Mock is_on property
    switch.pin_state = False
    sensor = MagicMock()
    sensor.get_measurement.return_value = 100
    return {
        "switch": switch,
        "ultrasonic_sensor_device": sensor,
    }
