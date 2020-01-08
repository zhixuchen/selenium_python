#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 18:04
# software: PyCharm

from test_case.case import *
from test_case.data import *
from report.image import *
if __name__ == '__main__':
    try:
        data = Data()
        driver = Driver()
        browser = driver.chrome_browser

        Case.login(browser,data)

        driver.tearDown()

    except Exception as e:
        print(e)
        catch_image(browser)
