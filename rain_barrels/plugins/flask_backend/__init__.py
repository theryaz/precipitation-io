from .flask_backend import FlaskBackend

def register(irrigation_system, config, logger):
    FlaskBackend(config, irrigation_system, logger).start()
