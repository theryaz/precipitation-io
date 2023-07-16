from unittest import IsolatedAsyncioTestCase, mock

from app import app
from rain_barrels.dto.manifold import Manifold
from rain_barrels.dto.rain_barrel import RainBarrel
from rain_barrels.dto.distance_sensor import DistanceSensor


class TestRainBarrelController(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        self.mock_rain_barrel_manifold = Manifold(
            distance_sensor=DistanceSensor(offset_cm=10, dead_zone_cm=12),
            rain_barrels=[
                RainBarrel(diameter=55, height=95),
                RainBarrel(diameter=55, height=95),
            ],
            current_volume_litres=0,
        )
        mock_get_rain_barrel_manifold = mock.patch(
            "rain_barrels.controllers.rain_barrels_controller.get_rain_barrel_manifold",
        ).start()
        mock_get_rain_barrel_manifold.return_value = self.mock_rain_barrel_manifold
        return super().setUp()

    def tearDown(self) -> None:
        mock.patch.stopall()

    async def test_get_available_water_litres_full(self):
        self.mock_rain_barrel_manifold.set_volume_by_measurement(10)
        response = await self.client.get("/rain_barrels/status")
        self.assertEqual(response.status_code, 200)
        response_body = await response.get_json()
        self.assertAlmostEqual(response_body.get("current_volume_litres", 0), 451.4, 1)
        self.assertAlmostEqual(response_body.get("percent_full"), 100, 1)

    async def test_get_available_water_litres_empty(self):
        self.mock_rain_barrel_manifold.set_volume_by_measurement(105)
        response = await self.client.get("/rain_barrels/status")
        self.assertEqual(response.status_code, 200)
        response_body = await response.get_json()
        self.assertAlmostEqual(response_body.get("current_volume_litres", 0), 0, 1)
        self.assertAlmostEqual(response_body.get("percent_full"), 0, 1)

    async def test_get_available_water_litres_medium(self):
        self.mock_rain_barrel_manifold.set_volume_by_measurement(37.2)
        response = await self.client.get("/rain_barrels/status")
        self.assertEqual(response.status_code, 200)
        response_body = await response.get_json()
        self.assertAlmostEqual(response_body.get("current_volume_litres", 0), 322.16, 1)
        self.assertAlmostEqual(response_body.get("percent_full"), 71.36, 1)
