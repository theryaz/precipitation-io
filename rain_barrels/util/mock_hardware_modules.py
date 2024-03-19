import sys
from unittest.mock import MagicMock


def mock_hardware_modules():
    """
    Call when running without real hardware to mock the IO modules
    """
    gpio_module_mock = MagicMock()
    sys.modules["RPi.GPIO"] = gpio_module_mock
    rpi_module_mock = MagicMock()
    sys.modules["RPi"] = rpi_module_mock
    smbus_module_mock = MagicMock()
    sys.modules["smbus"] = smbus_module_mock

    return {
        "gpio_module_mock": gpio_module_mock,
        "rpi_module_mock": rpi_module_mock,
        "smbus_module_mock": smbus_module_mock,
    }
