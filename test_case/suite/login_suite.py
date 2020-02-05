#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/10 18:47
# software: PyCharm
from test_case.suite import *

def suite():
    suite = unittest.TestSuite()
    suite.addTest(login_case.Login_Case('test_loginsSuccess'))
    suite.addTest(login_case.Login_Case('test_loginfail'))
    # suite.addTest(Login_Case('test_loginusernamefail'))
    # suite.addTest(Login_Case('test_nulluser'))
    # suite.addTest(Login_Case('test_nullpwd'))
    return suite

