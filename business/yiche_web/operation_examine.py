from business.yiche_web import *

if __name__ == '__main__':
    suite_tests = operation_examine_suite.suite()
    report_name = "REPORT"
    description = "运营中心审核"
    result = Report.report(suite_tests, report_name, description)
    if result:
        print("用例执行成功")
    else:
        print("用例执行失败")
