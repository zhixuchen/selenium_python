#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 18:04
# software: PyCharm

from test_case.case import *
from test_case.data import *
from report.image import *

import unittest
from BeautifulReport import BeautifulReport    #导入BeautifulReport
root_path = os.path.abspath(os.path.dirname(__file__)).split('selenium_python')[0]
path=root_path+"\\selenium_python\\"
if __name__ == '__main__':
    suite_tests = unittest.defaultTestLoader.discover(".",pattern="*tests.py",top_level_dir=None)     #"."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(suite_tests).report(filename='百度测试报告', description='搜索测试', log_path='.')    #log_path='.'把report放到当前目录下


