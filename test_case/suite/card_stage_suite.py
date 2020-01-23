#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/13 12:28
# software: PyCharm


from test_case.suite import *

def suite():
    suite = unittest.TestSuite()
    suite.addTest(card_stage_case.Card_Case('test_CardSuccess'))

    return suite
