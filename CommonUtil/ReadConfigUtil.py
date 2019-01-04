# coding=utf-8
import ConfigParser


def chekcSection(filePath, fileName, section):
    conf = ConfigParser.ConfigParser()
    conf.readfp(open(filePath + fileName))
    sections = conf.sections()
    if section in sections:
        return True
    else:
        return False


def checkOption(filePath, fileName, section):
    conf = ConfigParser.ConfigParser()
    conf.readfp(open(filePath + fileName))
    optins = conf.options(section)
    if optins:
        return True
    else:
        return False


def readConfig(filePath, fileName, section, option):
    conf = ConfigParser.ConfigParser()
    conf.readfp(open(filePath + fileName))
    svalue = conf.get(section, option)
    return svalue


def setConfig(filepath, filename, sesction, options):
    pass


# example print(readConfig('../config/','configfile.ini','mysqldb','ip'))
# print(chekcSection('../config/','configfile.ini','report'))
# read config information form ini file
print(checkOption('../config/', 'configfile.ini', 'apath'))
