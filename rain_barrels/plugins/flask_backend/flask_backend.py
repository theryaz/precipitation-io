from ..plugin import Plugin
from flask import Flask
from flask_cors import CORS


class FlaskBackend(Plugin):

    def __init__(self, config: dict, irrigation_system, logger):
        super().__init__(config, irrigation_system, logger)
        self.logger.debug(f"ApiBackend loaded with config: {config}")
        self.app = Flask(self.config.get("name", __name__))
        CORS(self.app)
        self.app.add_url_rule("/status", view_func=self.get_status, methods=["GET"])
        self.app.add_url_rule(
            "/turn_pump_on", view_func=self.turn_pump_on, methods=["POST"]
        )
        self.app.add_url_rule(
            "/turn_pump_off", view_func=self.turn_pump_off, methods=["POST"]
        )

    def _run(self):
        self.app.run(
            host=self.config.get("host", "localhost"),
            port=self.config.get("port", 8080),
        )

    def get_status(self):
        return {
            "pump_is_on": self.irrigation_system.pump_is_on,
            "total_capacity_litres": self.irrigation_system.total_capacity_litres,
            "current_volume_litres": self.irrigation_system.get_current_volume_litres(),
            "percent_full": self.irrigation_system.get_percent_full(),
        }

    def turn_pump_on(self):
        self.irrigation_system.turn_pump_on()
        return self.get_status()

    def turn_pump_off(self):
        self.irrigation_system.turn_pump_off()
        return self.get_status()
