# coding=utf-8
from CommonUtil.ReadConfigUtil import chekcSection, readConfig
from Common.TimeFormat import getLocalTime


def getFliePath(section, option):
    filePath = readConfig('../config/', 'configfile.ini', section, option)
    if filePath == '' or filePath == None or len(filePath) == 0:
        return '../' + section + '/'
    else:
        return filePath


def getFlieName(section, option):
    fileName = readConfig('../config/', 'configfile.ini', section, option)
    if fileName == '' or fileName == None or len(fileName) == 0:
        return getLocalTime() + '_'+section
    else:
        return getLocalTime() + '_'+fileName
