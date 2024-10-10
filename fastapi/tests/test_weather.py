import unittest
from types import NoneType

from post_router.utils import get_weather_data


class TestFactorial(unittest.TestCase):
    API_KEY = "8f27a4758ef564cfad2f354552ccb3da"

    def test_weather_moscow(self):
        res = get_weather_data("Moscow", api_key=self.API_KEY)
        self.assertIsInstance(res, dict)
        self.assertEqual(len(res), 6)

    def test_weather_unknown_city(self):
        res = get_weather_data("dfsfsfsfsdfs", api_key=self.API_KEY)
        self.assertIsInstance(res, NoneType)

    def test_weather_bad_api_key(self):
        res = get_weather_data("dfsfsfsfsdfs", api_key="ssddsse")
        self.assertIsInstance(res, NoneType)


if __name__ == '__main__':
    unittest.main()
