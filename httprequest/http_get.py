# coding=utf-8
import requests;


def http_get():
    url = 'http://www.sojson.com/open/api/weather/json.shtml'
    # headers = {"Content-Type": "application/json"}
    params = 'city=天津'
    response = requests.get(url=url, params=params)
    assert response.status_code == 200
    print (response.status_code)  # 11测试
    # jsondata=json.loads(response.text)
    #  jsonexp=parser('count')
    print response.text


if __name__ == "__main__":
    http_get()
