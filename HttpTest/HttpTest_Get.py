# coding=utf-8
import unittest
import requests
from Common.LogConfig import *


class GetWeather(unittest.TestCase):

    def setUp(self):
        self.url = 'http://www.sojson.com/open/api/weather/json.shtml'
        self.params = 'city=天津'
        # self.params=data+sign

    def test_beijng(self):
        response = requests.get(url=self.url, params=self.params)
        logging.debug(response.text)
        result = response.json()
        # print(result)
        # logging.log()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'Success !')

# if __name__ == "__main__":
#   GetWeather.test_beijng()
#   suit=unittest.TestSuite
#  suit.addTests(getWeather('test_beijng'))
# runner=unittest.TextTestRunner()
# runner.run(suit)
