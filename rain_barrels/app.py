from quart import Quart

from rain_barrels.controllers.rain_barrels_controller import rain_barrels

app = Quart(__name__)

app.register_blueprint(rain_barrels, url_prefix="/rain_barrels")


@app.route("/")
async def hello():
    return "Hello, world!"


if __name__ == "__main__":
    app.run()
