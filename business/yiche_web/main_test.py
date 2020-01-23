#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/23 16:52
# software: PyCharm
from business.yiche_web import *

if __name__ == '__main__':
    suite_tests=main_suite.suite()
    report_name="全面测试报告"
    description="全面测试"
    result=Report.report(suite_tests,report_name,description)
    if result:
        print("用例执行成功")
    else:
        print("用例执行失败")
