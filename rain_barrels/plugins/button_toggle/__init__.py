from .button_toggle import ButtonToggle

def register(irrigation_system, config, logger):
    ButtonToggle(config, irrigation_system, logger)
