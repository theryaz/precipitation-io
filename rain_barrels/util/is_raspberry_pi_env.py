import sys
from unittest.mock import MagicMock

IS_PI = None

def is_raspberry_pi_env() -> bool:
    global IS_PI
    if IS_PI is not None:
        return IS_PI
    try:
        import RPi.GPIO as gpio
        IS_PI = True
    except (ImportError, RuntimeError) as e:
        print(f"WARNING: Failed to import RPi.GPIO Using mock hardware modules. {e}")
        IS_PI = False
    return IS_PI
