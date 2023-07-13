from random import randint
from threading import Thread
from time import sleep

from rain_barrels.dto.manifold import Manifold


class RainBarrelDataCollector:
    """Collects sensor data from the rain barrel."""

    _collect_data_thread: Thread = None
    _collect_data_thread_stop: bool = False

    _distance_cm: float = 0

    def __init__(self, rain_barrel_manifold: Manifold):
        self.manifold = rain_barrel_manifold

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
        while self._collect_data_thread_stop is False:
            print("Collecting sensor data...")
            self._distance_cm = randint(25, 45)
            print(f"Mocking a distance of {self._distance_cm}cm")
            self.manifold.set_volume_by_measurement(self._distance_cm)
            print(self.manifold.print_status)
            sleep(5)
