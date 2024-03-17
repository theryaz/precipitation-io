from .lcd_display import LCDDisplay

def register(resevoir, config, logger):
    LCDDisplay(config, resevoir, logger).start()
