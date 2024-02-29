from rain_barrels.dto.distance_sensor import DistanceSensor
from rain_barrels.dto.reservoir import Reservoir
from rain_barrels.dto.rain_barrel import RainBarrel

"""
In-memory representation of a physical rain barrel reservoir.
"""

_RESERVOIR = Reservoir(
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
    _RESERVOIR.percent_full = percent_full


def get_rain_barrel_reservoir() -> Reservoir:
    """
    Return the current rain barrel reservoir in-memory representation.
    """
    return _RESERVOIR
