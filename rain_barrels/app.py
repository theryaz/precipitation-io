from quart import Quart

from rain_barrels.controllers.rain_barrels_controller import rain_barrels
from rain_barrels.models.rain_barrel_manifold import get_rain_barrel_manifold
from rain_barrels.models.sensor_data_collector import RainBarrelDataCollector

app = Quart(__name__)

app.register_blueprint(rain_barrels, url_prefix="/rain_barrels")


@app.route("/")
async def hello():
    return "Hello, world!"


if __name__ == "__main__":
    data_collector = RainBarrelDataCollector(get_rain_barrel_manifold())
    data_collector.start()
    app.run()
