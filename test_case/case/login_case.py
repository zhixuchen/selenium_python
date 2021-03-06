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
        self.log = Logs()
        self.data = Data()
        self.image = Image()  ## 初始化截屏功能

    def login(self):
        try:
            url = self.data.url
            self.browser.get(url)
        except Exception as e:
            self.log.log_error(e)
            self.image.catch_image(self.browser)

    def loginbypwd(self, account, pwd):  # 密码登录
        try:
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(pwd)
            find_elements(self.browser, By.TAG_NAME, "button")[0].click()
        except Exception as e:
            self.log.log_error(e)
            self.image.catch_image(self.browser)

    def loginbysms(self, account, sms_code):  # 验证码登录
        try:
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)  # 账号输入框
            find_elements(self.browser, By.TAG_NAME, "button")[1].click()  # 登陆下方,登录方式切换按钮
            find_elements(self.browser, By.TAG_NAME, "button")[0].click()  # 获取验证码按钮
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(sms_code)  # 验证码输入框
            find_elements(self.browser, By.TAG_NAME, "button")[1].click()  # 登录
        except Exception as e:
            self.log.log_error(e)
            self.image.catch_image(self.browser)

    def check_Equal(self, first, second, msg=None):
        try:
            self.assertEqual(first, second, msg=None)
        except AssertionError:
            self.image.catch_image(self.browser)
            raise

    def home_page(self):
        '''首页文案元素'''
        self.login()
        system_name = find_element(self.browser, By.XPATH, '//*[@id="app"]/div/div/div[1]/span')
        self.check_Equal(system_name.text, '林润云收单系统')
        welcome_name = find_element(self.browser, By.CLASS_NAME, 'login-form-title')
        self.check_Equal(welcome_name.text, '欢迎登录林润云收单系统')
        account_hint_message = find_element(self.browser, By.XPATH, '//*[@id="app"]/div/div/div[2]/div/form/div/div[1]/div/div/input').get_attribute('placeholder')
        self.check_Equal(account_hint_message, '请输入手机号码')
        passwordd_hint_message = find_element(self.browser, By.XPATH, '//*[@id="app"]/div/div/div[2]/div/form/div/div[2]/div/div/input').get_attribute('placeholder')
        self.check_Equal(passwordd_hint_message, '请输入密码')
        login_button = find_element(self.browser, By.XPATH, '//*[@id="app"]/div/div/div[2]/div/form/button[1]/span').text
        self.check_Equal(login_button, '登录')
        message_login_button = find_element(self.browser, By.XPATH, '//*[@id="app"]/div/div/div[2]/div/form/button[2]/span').text
        self.check_Equal(message_login_button, '手机验证码登录')


    def test_loginsSuccessbypwd(self):
        '''登录成功通过密码'''
        account = self.data.get_account("xs_account")
        pwd = self.data.get_pwd("xs_pwd")
        self.login()
        self.loginbypwd(account, pwd)
        tip = find_element(self.browser, By.CLASS_NAME, "header-title").text
        self.check_Equal(tip, '林润云系统')

    def test_loginsSuccessbysms_code(self):
        '''登录成功通过验证码'''
        account = self.data.get_account("xs_account")
        sms_code = self.data.sms_code
        self.login()
        self.loginbysms(account, sms_code)
        tip = find_element(self.browser, By.CLASS_NAME, "header-title").text
        self.check_Equal(tip, '林润云系统')

    def test_error_account(self):
        '''用户名不存在'''
        account = self.data.get_account("error_account")
        pwd = self.data.get_pwd("xs_pwd")
        self.login()
        self.loginbypwd(account, pwd)
        error_tip = find_element(self.browser, By.CLASS_NAME, "el-form-item__error").text
        self.check_Equal(error_tip, '密码错误')
        error_tip = find_element(self.browser, By.CLASS_NAME, "el-notification__content").text
        self.check_Equal(error_tip, '用户不存在')

    def test_error_pwd(self):
        '''密码错误'''
        account = self.data.get_account("xs_account")
        pwd = "666666"
        self.login()
        self.loginbypwd(account, pwd)
        error_tip = find_element(self.browser, By.CLASS_NAME, "el-form-item__error").text
        self.check_Equal(error_tip, '密码错误')
        error_tip = find_element(self.browser, By.CLASS_NAME, "el-notification__content").text
        self.check_Equal(error_tip, '账号或密码输入错误，或账户被禁用，请联系管理员')

    def test_nulluser(self):
        '''用户名为空'''
        account = ""
        pwd = self.data.get_pwd("xs_pwd")
        self.login()
        self.loginbypwd(account, pwd)
        error_tip = find_element(self.browser, By.CLASS_NAME, "el-form-item__error").text
        self.check_Equal(error_tip, '请输入手机号码')

    def test_nullpwd(self):
        '''密码为空'''
        account = self.data.get_account("xs_account")
        pwd = ""
        self.login()
        self.loginbypwd(account, pwd)
        error_tip = find_element(self.browser, By.CLASS_NAME, "el-form-item__error").text
        self.check_Equal(error_tip, '密码不能为空')

    def test_null_Verify(self):
        '''验证码为空'''
        account = self.data.get_account("xs_account")
        sms_code = ""
        self.login()
        self.loginbysms(account, sms_code)
        error_tip = find_element(self.browser, By.CLASS_NAME, "el-form-item__error").text
        self.check_Equal(error_tip, '请输入验证码')

    def test_error_Verify(self):
        '''验证码错误'''
        account = self.data.get_account("xs_account")
        sms_code = "666666"
        self.login()
        self.loginbysms(account, sms_code)
        time.sleep(1)
        error_tip = find_elements(self.browser, By.CLASS_NAME, "el-notification__content")
        if len(error_tip) == 2:
            self.check_Equal(error_tip[0].text, '发送间隔时间小于60秒')
            self.check_Equal(error_tip[1].text, '请输入正确的验证码')
        else:
            self.check_Equal(error_tip[0].text, '请输入正确的验证码')

    def tearDown(self):
        self.log.log_info("登录测试结束")
        time.sleep(3)
        self.driver.tearDown()


if __name__ == '__main__':
    unittest.main()

    # print(a.account)
    # login()
