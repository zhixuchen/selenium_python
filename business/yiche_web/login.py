#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/10 11:10
# software: PyCharm


from report import *

from test_case.suite.login_suite import *


if __name__ == '__main__':
    suite_tests=suite()
    report_name="测试报告"
    description="登录验证"
    result=Report.report(suite_tests,report_name,description)
    if result:
        print("用例执行成功")
    else:
        print("用例执行失败")






