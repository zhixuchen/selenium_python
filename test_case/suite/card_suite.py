#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/13 12:28
# software: PyCharm


from test_case.case.card_case import *

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Login_Case('test_loginsSuccess'))
    suite.addTest(Card_Case('test_CardSuccess'))

    return suite
