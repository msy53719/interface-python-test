# coding=utf-8
from Common.GetFileConfig import *


def getReportPath():
    return getFliePath('report', 'reportpath')


def getReportName():
    if getFlieName('report', 'reportname').endswith('.html'):
        return getFlieName('report', 'reportname')
    else:
        return getFlieName('report', 'reportname') + '.html'


def getReportTitle():
    title = readConfig('../config/', 'configfile.ini', 'report', 'title')
    if title == '' or title == None or len(title) == 0:
        return 'this is a test report'
    else:
        return title


def getReportDes():
    Des = readConfig('../config/', 'configfile.ini', 'report', 'Des')
    if Des == '' or Des == None or len(Des) == 0:
        return 'this is a test Des'
    else:
        return Des
