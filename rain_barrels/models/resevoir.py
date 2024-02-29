from util.logger import LOGGER
from volume_sensor import VolumeSensor
from tank import Tank

class Resevoir():
    
    def __init__(self, name: str, volume_sensor: VolumeSensor, tanks: list[Tank] = []):
        self.name = name
        self.volume_sensor = volume_sensor
        self.tanks = tanks
    
    name: str
    volume_sensor: VolumeSensor
    tanks: list[Tank]
    current_volume_litres: int = 0

    def get_volume() -> int:
        '''
        Returns the current volume of the resesoir. 0-100%
        '''
        pass

    def turn_pump_on():
        LOGGER.info('Pump turned on')

    def turn_pump_off():
        LOGGER.info('Pump turned off')
        
    @property
    def total_capacity_litres(self):
        """
        The total available capacity of the resevoir in litres
        """
        return sum([tank.capacity_litres for tank in self.tanks])

    @property
    def percent_full(self):
        return (self.current_volume_litres / self.total_capacity_litres) * 100

    @property
    def height(self):
        return self.rain_barrels[0].height

    @property
    def print_status(self):
        return f"{self.name} Resevoir Status: {round(self.percent_full, 2)}% full ({round(self.current_volume_litres, 2)}/{round(self.total_volume_litres)} L)"

    @property
    def print_status_short(self):
        return f"{round(self.percent_full, 2)}% - {round(self.current_volume_litres, 2)}L"
    
    def _get_water_level(self, distance_cm: float, height: float) -> float:
        """
        Returns the water level in centimeters
        _. <- Sensor
        |         |  |  |
        |         |  |  | <- Offset
        ++++++++  |  | <- Dead zone
        |      |  |  <- Distance
        |------| <- Water level
        |ssssss|
        ++++++++

        Given the height of the barrel, the distance from the sensor minus the offset is the waterlevel.

        The deadzone is factored in if the offset is less than the deadzone,
        the water should be considered full in this case since we can't get an accurate reading, but know it's close to full.

        """
        if distance_cm <= self.dead_zone_cm:
            return height  # Assume barrel is full
        return height - max(0, distance_cm - self.offset_cm)

    def _measure_current_volume(self):
        water_level_cm = self._get_water_level(self.volume_sensor.measure(), self.height)
        self.current_volume_litres = (
            sum(
                [
                    tank.compute_volume_full(water_level_cm)
                    for tank in self.tanks
                ]
            )
        )
        return {
            "volume_litres": self.current_volume_litres,
            "percent_full": self.percent_full,
        }