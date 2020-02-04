from business.yiche_web import *

if __name__ == '__main__':
    suite_tests = company_examine_suite.suite()
    report_name = "测试报告"
    description = "公司审核初审"
    result = Report.report(suite_tests, report_name, description)
    if result:
        print("用例执行成功")
    else:
        print("用例执行失败")
