from os import getenv
from random import randint
from threading import Thread
from time import sleep

from rain_barrels.dto.manifold import Manifold
from rain_barrels.drivers.ultrasonic_sensor_dev import UltrasonicSensorDevice
from rain_barrels.models.lcd_display import _LCDDisplay

TRIG_PIN = getenv("TRIG_PIN") or 38
ECHO_PIN = getenv("ECHO_PIN") or 40

class UltrasonicSensorDataCollector:
    """Collects sensor data from the rain barrel."""

    _collect_data_thread: Thread = None
    _collect_data_thread_stop: bool = False
    _polling_rate: int = 5

    _distance_cm: float = 0

    def __init__(self, rain_barrel_manifold: Manifold, lcd_display: _LCDDisplay):
        self.manifold = rain_barrel_manifold
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
            self._distance_cm = self.sensor.get_measurement()
            print(f"Reading distance of {self._distance_cm}cm")
            self.manifold.set_volume_by_measurement(self._distance_cm)
            print(self.manifold.print_status)
            self.display.display_text = [
                f"Distance: {self._distance_cm}cm",
                f"{self.manifold.print_status_short}"
            ]
            sleep(self._polling_rate)
