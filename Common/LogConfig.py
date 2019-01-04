# coding=utf-8
import logging
from Common.GetFileConfig import *

LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S %p'


def getLogPath():
    return getFliePath('log', 'logpath')


def getLogFileName():
    if getFlieName('log', 'logname').endswith('.log'):
        return getFlieName('log', 'logname')
    else:
        return getFlieName('log', 'logname') + '.log'


logging.basicConfig(filename=getLogPath() + getLogFileName(), level=logging.DEBUG, format=LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    filemode='w', encoding='utf-8'
                    )
