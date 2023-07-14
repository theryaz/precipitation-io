from quart import Quart
from rain_barrels.util.mock_hardware_modules import mock_hardware_modules
mock_hardware_modules()

from rain_barrels.controllers.rain_barrels_controller import rain_barrels
from rain_barrels.models.rain_barrel_manifold import get_rain_barrel_manifold
from rain_barrels.models.sensor_data_collector import RainBarrelDataCollector
from rain_barrels.models.lcd_display import LCDDisplay

data_collector = RainBarrelDataCollector(get_rain_barrel_manifold())


app = Quart(__name__)

app.register_blueprint(rain_barrels, url_prefix="/rain_barrels")

@app.after_serving
def cleanup():
    print("Cleaning up threads...")
    data_collector.stop()
    data_collector.stop()


if __name__ == "__main__":
    data_collector.start()
    LCDDisplay.start()
    app.run()
