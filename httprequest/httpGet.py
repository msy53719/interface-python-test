# coding=utf-8
import requests;
import json;


def http_post():
    url = 'https://kyfw.12306.cn/passport/web/login'
    headers = {"Content-Type": "application/json"}
    data = {
        "username": "CHN_D00000",
        "password": "REDEEM",
    }
    r = requests.post(url=url, json=data, headers=headers)
    print (r.status_code)  # 11测试
    print (r.text)
    print '测试'


if __name__ == "__main__":
    http_post()
