from quart import Blueprint

from rain_barrels.models.rain_barrel_manifold import get_rain_barrel_manifold

rain_barrels = Blueprint("rain_barrels", __name__)


@rain_barrels.route("/status")
def get_available_water_litres():
    rb = get_rain_barrel_manifold()
    return {
        "current_volume_litres": rb.current_volume_litres,
        "percent_full": rb.percent_full,
    }
