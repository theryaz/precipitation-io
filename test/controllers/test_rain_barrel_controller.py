from unittest import IsolatedAsyncioTestCase, mock

from rain_barrels.app import app
from rain_barrels.dto.manifold import Manifold
from rain_barrels.dto.rain_barrel import RainBarrel


class TestRainBarrelController(IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        self.mock_rain_barrel_manifold = Manifold(
            rain_barrels=[
                RainBarrel(diameter=22, height=32),
                RainBarrel(diameter=22, height=32),
            ],
            percent_full=32,
        )
        mock_get_rain_barrel_manifold = mock.patch(
            "rain_barrels.controllers.rain_barrels_controller.get_rain_barrel_manifold",
        ).start()
        mock_get_rain_barrel_manifold.return_value = self.mock_rain_barrel_manifold
        return super().setUp()

    def tearDown(self) -> None:
        mock.patch.stopall()

    async def test_get_available_water_litres(self):
        response = await self.client.get("/rain_barrels/water_litres")
        self.assertEqual(response.status_code, 200)
        response_body = await response.get_json()
        self.assertAlmostEqual(response_body["available_water_litres"], 7.78, 1)
        self.assertAlmostEqual(response_body["percent_full"], 32)
