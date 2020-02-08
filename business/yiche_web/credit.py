#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 18:04
# software: PyCharm
from business.yiche_web import *

if __name__ == '__main__':
    suite_tests=credit_suite.suite()
    report_name="REPORT"
    description="提交征信"
    result=Report.report(suite_tests,report_name,description)
    if result:
        print("用例执行成功")
    else:
        print("用例执行失败")
