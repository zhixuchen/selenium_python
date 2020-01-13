#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/13 12:14
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

    def tearDown(self):
        print("登录测试结束")
        globals()["browser"]=self.browser
        globals()["driver"] = self.driver

class Credit_Case(unittest.TestCase):
    def setUp(self):
        self.driver = globals()["driver"]
        self.browser=globals()["browser"]

    def credit(self):
        find_elementbytext(self.browser,By.TAG_NAME,"a","征信进件").click()

    def test_CreditSuccess(self):
        TestData=Test_Data()
        root_path = os.path.abspath(os.path.dirname(__file__)).split('selenium_python')[0]
        path = root_path + "selenium_python\\test_case\\data\\image\\"
        self.credit()
        div_fields=find_element(self.browser,By.CLASS_NAME,"comp-form-item-fields")
        fields_elements=div_fields.find_elements_by_tag_name("label")
        for i in range(0,len(fields_elements)):
            self.assertEqual(fields_elements[i].text,TestData.credit_input_titles[i])
        div_image = find_element(self.browser, By.CLASS_NAME, "image-field-row")
        image_elements = div_image.find_elements_by_tag_name("label")
        for i in range(0,len(image_elements)):
            self.assertEqual(image_elements[i].text,TestData.credit_image_titles[i])
        images= find_elements(self.browser,By.CLASS_NAME,"image-pane")
        for i in range(len(images)):
            images[i].click()
            upload_image(path,TestData.credit_image_titles[i])
            while True:
                if "重传"!=images[i].find_element_by_tag_name("button").text:
                    time.sleep(1)
                    print("上传还未完成等待1秒")
                    if "重传"==images[i].find_element_by_tag_name("button").text:
                        print("上传完成")
                        break
                else:
                    print("上传完成")
                    break









    def tearDown(self):
        print("测试结束")
        # self.driver.tearDown()


if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        print("")
