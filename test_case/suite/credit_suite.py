#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/13 12:28
# software: PyCharm


from test_case.suite import *

def suite():
    suite = unittest.TestSuite()
    suite.addTest(credit_case.Credit_Case('test_E_X_Credit'))
    suite.addTest(credit_case.Credit_Case('test_E_E_Credit'))

    return suite
