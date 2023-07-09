from rain_barrels.dto.manifold import Manifold
from rain_barrels.dto.rain_barrel import RainBarrel

"""
In-memory representation of a physical rain barrel manifold.
"""

_RAIN_BARRELS = Manifold(
    rain_barrels=[
        RainBarrel(
            diameter=22,
            height=32,
        ),
        RainBarrel(
            diameter=22,
            height=32,
        ),
    ],
    percent_full=0,
)


def set_percent_full(percent_full: int):
    _RAIN_BARRELS.percent_full = percent_full


def get_rain_barrel_manifold() -> Manifold:
    """
    Return the current rain barrel manifold in-memory representation.
    """
    return _RAIN_BARRELS
