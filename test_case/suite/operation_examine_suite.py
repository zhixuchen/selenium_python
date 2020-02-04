#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/13 12:28
# software: PyCharm


from test_case.suite import *

def suite():
    suite = unittest.TestSuite()
    suite.addTest(operation_examine_case.Operation_Examine('test_ExamineFirstSuccess'))
    suite.addTest(operation_examine_case.Operation_Examine('test_ExamineSecondSuccess'))
    suite.addTest(operation_examine_case.Operation_Examine('test_ExamineThirdSuccess'))

    return suite
