from .lcd_display import LCDDisplay

def register(irrigation_system, config, logger):
    LCDDisplay(config, irrigation_system, logger).start()
