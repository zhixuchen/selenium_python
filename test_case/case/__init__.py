#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/7 16:25
# software: PyCharm

import numpy
from selenium.webdriver.common.by import By
from test_case.data import Data
from function.element import *
from report.image import *
class Case():
    def login(browser,data):
        try:
            url = data.url
            account = data.account
            pwd = data.pwd
            sms_code = data.sms_code
            browser.get(url)
            random = numpy.random.randint(0, 2, 1)
            if random == 0:  # 密码登录
                find_elements(browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
                find_elements(browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(pwd)
                find_elements(browser, By.TAG_NAME, "button")[0].click()

            elif random == 1:  # 验证码登录
                find_elements(browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
                find_elements(browser, By.TAG_NAME, "button")[1].click()
                find_elements(browser, By.TAG_NAME, "button")[0].click()
                find_elements(browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(sms_code)
                find_elements(browser, By.TAG_NAME, "button")[1].click()
        except Exception as e:
            catch_image(browser)


if __name__ == '__main__':
    data=Data()
    driver = Driver()
    browser = driver.chrome_browser
    Case().login(browser,data)
    # print(a.account)
    # login()
