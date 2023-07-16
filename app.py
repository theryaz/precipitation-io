from quart import Quart
from rain_barrels.util.is_raspberry_pi_env import is_raspberry_pi_env
from rain_barrels.util.mock_hardware_modules import mock_hardware_modules

if not is_raspberry_pi_env():
    mock_hardware_modules()

import RPi.GPIO as GPIO

from rain_barrels.controllers.rain_barrels_controller import rain_barrels
from rain_barrels.models.rain_barrel_reservoir import get_rain_barrel_reservoir
from rain_barrels.models.sensor_data_collector import UltrasonicSensorDataCollector
from rain_barrels.models.lcd_display import LCDDisplay

data_collector = UltrasonicSensorDataCollector(get_rain_barrel_reservoir(), LCDDisplay)

app = Quart(__name__)

app.register_blueprint(rain_barrels, url_prefix="/rain_barrels")

@app.after_serving
def cleanup():
    print("Cleaning up threads...")
    data_collector.stop()
    LCDDisplay.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    data_collector.start()
    LCDDisplay.start()
    app.run()
