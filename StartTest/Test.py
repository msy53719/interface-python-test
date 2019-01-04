# coding=utf-8
import sys

sys.path.append('~/pythonSpace/InterfaceTest')  # 为命令行编译提供支持
sys.path.append('~/pythonSpace/InterfaceTest/StartTest')  # 为命令行编译提供支持
from HttpTest.HttpTest_Get import *
from HtmlReportUtil.HTMLTestRunner import HTMLTestRunner
from Common.ReportConfig import *
import unittest

# print(sys.path)
if __name__ == '__main__':
    suite = unittest.makeSuite(GetWeather)
    fp = file(getReportPath() + getReportName(), 'wb')
    runner = HTMLTestRunner(fp, title=getReportTitle(), description=getReportDes())
    runner.run(suite)
