from quart import Quart

from rain_barrels.controllers.rain_barrels_controller import rain_barrels
from rain_barrels.models.rain_barrel_manifold import get_rain_barrel_manifold
from rain_barrels.models.sensor_data_collector import RainBarrelDataCollector

data_collector = RainBarrelDataCollector(get_rain_barrel_manifold())

app = Quart(__name__)

app.register_blueprint(rain_barrels, url_prefix="/rain_barrels")

app.after_serving(data_collector.stop)


if __name__ == "__main__":
    data_collector.start()
    app.run()
