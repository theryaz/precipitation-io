from rain_barrels.dto.distance_sensor import DistanceSensor
from rain_barrels.dto.manifold import Manifold
from rain_barrels.dto.rain_barrel import RainBarrel

"""
In-memory representation of a physical rain barrel manifold.
"""

_RAIN_BARRELS = Manifold(
    distance_sensor=DistanceSensor(offset_cm=30, dead_zone_cm=25),
    rain_barrels=[
        RainBarrel(
            diameter=2.54,
            height=95,
        ),
        RainBarrel(
            diameter=55,
            height=95,
        ),
        RainBarrel(
            diameter=55,
            height=95,
        ),
    ],
    current_volume_litres=0,
)


def set_percent_full(percent_full: int):
    _RAIN_BARRELS.percent_full = percent_full


def get_rain_barrel_manifold() -> Manifold:
    """
    Return the current rain barrel manifold in-memory representation.
    """
    return _RAIN_BARRELS
