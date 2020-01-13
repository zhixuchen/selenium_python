#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/7 16:25
# software: PyCharm

from test_case.case import *
class Login_Case(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.browser=self.driver.chrome_browser

    def login(self,data):
        try:
            url = data.url
            account = data.account
            pwd = data.pwd
            sms_code = data.sms_code
            self.browser.get(url)
            random = numpy.random.randint(0, 2, 1)
            random=0
            if random == 0:  # 密码登录
                find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
                find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(pwd)
                find_elements(self.browser, By.TAG_NAME, "button")[0].click()

            elif random == 1:  # 验证码登录
                find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
                find_elements(self.browser, By.TAG_NAME, "button")[1].click()
                find_elements(self.browser, By.TAG_NAME, "button")[0].click()
                find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(sms_code)
                find_elements(self.browser, By.TAG_NAME, "button")[1].click()

        except Exception as e:
            print(e)
            catch_image(self.browser)

    def test_loginsSuccess(self):
        '''登录成功'''
        data = Data()
        self.login(data)
        tip = find_element(self.browser,By.CLASS_NAME,"header-title").text
        self.assertEqual(tip, '林润云收单系统')




    # def test_nulluser(self):
    #     '''用户名为空'''
    #
    #     self.login('', '', '')
    #     self.driver.switch_to.alert().accept()
    #     nullusererror = self.driver.switch_to.alert().text
    #     self.assertEqual(nullusererror, '请输入管理员账号')

    # def test_nullpwd(self):
    #     '''密码为空'''
    #
    #     self.login('13620180611', '', '')
    #     self.driver.switch_to.alert().accept()
    #     nullpassword = self.driver.switch_to.alert().text
    #     self.assertEqual(nullpassword, '请输入管理员密码')
    #
    # def test_nulltxtVerify(self):
    #     self.login('13620180611', 'Aa654321', '')
    #
    #     self.driver.switch_to.alert().accept()
    #     nulltxtVerify = self.driver.switch_to.alert().text
    #     self.assertEqual(nulltxtVerify, '请输入验证码')

    def tearDown(self):
        print("登录测试结束")



        self.driver.tearDown()



if __name__ == '__main__':
    unittest.main()

    # print(a.account)
    # login()
