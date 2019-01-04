# coding=utf-8
import time


def getLocalTime():
    str = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return str

def getLocal_Time():
    str = time.strftime("%Y-%m-%d:%H:%M:%S", time.localtime())
    return str


print(getLocal_Time())