#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/10 18:47
# software: PyCharm
from test_case.suite import *

def suite():
    suite = unittest.TestSuite()
    suite.addTest(login_case.Login_Case('test_loginsSuccessbypwd'))
    suite.addTest(login_case.Login_Case('test_loginsSuccessbysms_code'))
    suite.addTest(login_case.Login_Case('test_nulluser'))
    suite.addTest(login_case.Login_Case('test_nullpwd'))
    suite.addTest(login_case.Login_Case('test_nulltxtVerify'))
    suite.addTest(login_case.Login_Case('test_error_Verify'))
    suite.addTest(login_case.Login_Case('test_error_account'))
    suite.addTest(login_case.Login_Case('test_error_pwd'))

    return suite

