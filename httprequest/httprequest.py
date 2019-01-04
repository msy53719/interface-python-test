# coding=utf-8
import requests;
import json;


def http_post():
    url = 'http://10.232.138.137:8230/v1/verifications'
    headers = {"Content-Type": "application/json"}
    data = {
        "channel": "CHN_D00000",
        "transType": "REDEEM",
        "flowId": "213245678901234567890",
        "clientId": "CHN_TRANSFORMER",
        "transDatetime": 11111
    }
    r = requests.post(url=url, json=data, headers=headers)
    print (r.status_code)  # 11测试
    print (r.text)
    print '测试'


if __name__ == "__main__":
    http_post()
