import sys
from unittest.mock import MagicMock

def is_raspberry_pi_env() -> bool:
    try:
        import RPi.GPIO as gpio
        is_pi = True
    except (ImportError, RuntimeError):
        is_pi = False
    return is_pi
