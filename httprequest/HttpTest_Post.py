#coding=utf-8
import unittest
import requests
import logging

class getWeather(unittest.TestCase):

    def setUp(self):
        self.url='http://www.sojson.com/open/api/weather/json.shtml'
        self.headers = {"Content-Type": "application/json"}
        self.data = {
        "channel": "CHN_D00000",
        "transType": "REDEEM",
        "flowId": "213245678901234567890",
        "clientId": "CHN_TRANSFORMER",
        "transDatetime": 11111
    }

    def test_beijng(self):
        response = requests.post(url=self.url, json=self.data, headers=self.headers)
        result=response.json()
        print(result)
        #logging.log()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'], 'Success !')

if __name__ == "__main__":
    suit=unittest.TestSuite
    suit.addTests(getWeather('test_beijng'))
    runner=unittest.TextTestRunner()
    runner.run(suit)
