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
        self.data = Data()

    def login(self):
        try:
            url = self.data.url
            self.browser.get(url)
        except Exception as e:
            print(e)
            catch_image(self.browser)

    def test_loginbypwd(self): # 密码登录
        try:

            account = self.data.get_account("xs_account")
            pwd = self.data.get_pwd("xs_pwd")
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(pwd)
            find_elements(self.browser, By.TAG_NAME, "button")[0].click()
        except Exception as e:
            print(e)
            catch_image(self.browser)

    def test_loginbysms(self): # 验证码登录
        try:
            account = self.data.get_account("xs_account")
            sms_code = self.data.sms_code
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account) #账号输入框
            find_elements(self.browser, By.TAG_NAME, "button")[1].click() # 登陆下方,登录方式切换按钮
            find_elements(self.browser, By.TAG_NAME, "button")[0].click() # 获取验证码按钮
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(sms_code) # 验证码输入框
            find_elements(self.browser, By.TAG_NAME, "button")[1].click() # 登录
        except Exception as  e:
            print(e)
            catch_image(self.browser)

    def test_loginsSuccess(self):
        '''登录成功'''
        self.login()
        self.test_loginbypwd()
        tip = find_element(self.browser, By.CLASS_NAME, "header-title").text
        self.assertEqual(tip, '林润云系统')

    def test_nulluser(self):
        '''用户名为空-tang'''
        self.login()
        pwd = self.data.get_pwd("xs_pwd")
        find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(pwd)
        find_elements(self.browser, By.TAG_NAME, "button")[0].click()
        time.sleep(1)
        error_tip = find_element(self.browser, By.CLASS_NAME,"el-form-item__error").text
        print("error_tip:"+error_tip)
        self.assertEqual(error_tip, '请输入手机号码')

    def test_nullpwd(self):
        '''密码为空-tang'''
        self.login()
        account = self.data.get_account("xs_account")
        find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
        find_elements(self.browser, By.TAG_NAME, "button")[0].click()
        error_tip = find_element(self.browser, By.CLASS_NAME, "el-form-item__error").text
        self.assertEqual(error_tip, '密码不能为空')

    # def test_nulltxtVerify(self):
    #     '''验证码为空-huyx'''

    # def test_error_pwd(self):
    #     '''密码错误-niu'''

    # def test_error_account(self):
    #     '''用户名错误-ouyf'''

    # def test_error_Verify(self):
    #     '''验证码错误-huyx'''



    def tearDown(self):
        self.log.log_info("登录测试结束")
        time.sleep(3)

        self.driver.tearDown()


if __name__ == '__main__':
    unittest.main()

    # print(a.account)
    # login()
