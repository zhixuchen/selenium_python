#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/7 16:25
# software: PyCharm

from test_case.case import *


class Login_Case(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.browser = self.driver.chrome_browser
        self.log=Logs()

    def login(self):
        try:
            data = Data()
            url = data.url
            self.browser.get(url)
        except Exception as e:
            print(e)
            catch_image(self.browser)

    def test_loginbypwd(self):
        try:
            data = Data()
            account = data.get_account("xs_account")
            pwd = data.get_pwd("xs_pwd")
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(pwd)
            find_elements(self.browser, By.TAG_NAME, "button")[0].click()
        except Exception as e:
            print(e)
            catch_image(self.browser)

    def test_loginbysms(self):
        try:
            data = Data()
            account = data.get_account("xs_account")
            sms_code = data.sms_code
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
            find_elements(self.browser, By.TAG_NAME, "button")[1].click()
            find_elements(self.browser, By.TAG_NAME, "button")[0].click()
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(sms_code)
            find_elements(self.browser, By.TAG_NAME, "button")[1].click()
        except Exception as  e:
            print(e)
            catch_image(self.browser)

    def test_loginsSuccess(self):
        '''登录成功'''
        self.login()
        self.test_loginbypwd()
        tip = find_element(self.browser, By.CLASS_NAME, "header-title").text
        self.assertEqual(tip, '林润云系统')

    def test_loginnullcode(self):
        try:
            data = Data()
            account = data.get_account("xs_account")
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
            find_elements(self.browser, By.TAG_NAME, "button")[1].click()
            find_elements(self.browser, By.TAG_NAME, "button")[1].click()
        except Exception as  e:
            print(e)
            catch_image(self.browser)

    def test_nulltxtVerify(self):
        '''验证码为空-huyx'''
        self.login()
        self.test_loginnullcode()
        tip = find_element(self.browser, By.XPATH, "//*[@id='app']/div/div/div[2]/div/form/div/div[2]/div/div[2]").text
        self.assertEqual(tip, '请输入验证码')

    def test_loginerrorcode(self):
        try:
            data = Data()
            account = data.get_account("xs_account")
            sms_code = "666666"
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
            find_elements(self.browser, By.TAG_NAME, "button")[1].click()
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(sms_code)
            find_elements(self.browser, By.TAG_NAME, "button")[1].click()
            time.sleep(1)
        except Exception as  e:
            print(e)
            catch_image(self.browser)

    def test_error_Verify(self):
        '''验证码错误-huyx'''
        self.login()
        self.test_loginerrorcode()
        tip = find_element(self.browser, By.XPATH, "/html/body/div[2]/div/div[1]").text
        self.assertEqual(tip, '请输入正确的验证码')


    def tearDown(self):
        self.log.log_info("登录测试结束")
        time.sleep(10)

        self.driver.tearDown()


if __name__ == '__main__':
    unittest.main()

    # print(a.account)
    # login()
