#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/13 12:28
# software: PyCharm


from test_case.suite import *

def suite():
    suite = unittest.TestSuite()
    suite.addTest(company_examine_case.Company_Examine('test_ExamineSuccess'))

    return suite
