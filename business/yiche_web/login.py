#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/10 11:10
# software: PyCharm


from report import *
import unittest
from test_case.case.login_case import Login_Case

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Login_Case('test_loginsSuccess'))
    # suite.addTest(Login_Case('test_loginfail'))
    # suite.addTest(Login_Case('test_loginusernamefail'))
    # suite.addTest(Login_Case('test_nulluser'))
    # suite.addTest(Login_Case('test_nullpwd'))
    return suite


if __name__ == '__main__':
    suite_tests=suite()
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_name="测试报告"+picture_time
    description="登录验证"
    build_report(suite_tests,report_name,description)




