from os import getenv
from random import randint
from threading import Thread
from time import sleep

from rain_barrels.plugins.____lcd_display import _LCDDisplay
from rain_barrels.drivers.ultrasonic_sensor_dev import UltrasonicSensorDevice
from rain_barrels.dto.reservoir import Reservoir

TRIG_PIN = getenv("TRIG_PIN") or 40
ECHO_PIN = getenv("ECHO_PIN") or 38


class UltrasonicSensorDataCollector:
    """Collects sensor data from the rain barrel."""

    _collect_data_thread: Thread = None
    _collect_data_thread_stop: bool = False
    _polling_rate: int = 1

    _distance_cm: float = 0

    def __init__(self, rain_barrel_reservoir: Reservoir, lcd_display: _LCDDisplay):
        self.reservoir = rain_barrel_reservoir
        self.sensor = UltrasonicSensorDevice(TRIG_PIN, ECHO_PIN)
        self.display = lcd_display

    @property
    def sensor_data(self):
        """Return the current sensor data."""
        return {
            "distance_cm": self._distance_cm,
        }

    def start(self):
        """Start collecting sensor data."""
        if self._collect_data_thread is None:
            print("Starting Data Collector...")
            self._collect_data_thread_stop = False
            self_collect_data_thread = Thread(target=self._collect_data)
            self_collect_data_thread.start()

    def stop(self):
        """Stop collecting sensor data."""
        if self._collect_data_thread is not None:
            print("Stopping Data Collector...")
            self._collect_data_thread_stop = True
            self._collect_data_thread.join()
            self._collect_data_thread = None

    def _collect_data(self):
        """Collect sensor data."""
        while not self._collect_data_thread_stop:
            sleep(self._polling_rate)
            self._distance_cm = self.sensor.get_measurement()
            print(f"Reading distance of {self._distance_cm}cm")
            self.reservoir.set_volume_by_measurement(self._distance_cm)
            print(self.reservoir.print_status)
            self.display.display_text = [
                f"Distance: {self._distance_cm}cm",
                f"{self.reservoir.print_status_short}",
            ]
