#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/13 12:14
# software: PyCharm
from test_case.case import *

TestData = Test_Data()
data = Data()
root_path = os.path.abspath(os.path.dirname(__file__)).split('selenium_python')[0]
path = root_path + "selenium_python\\test_case\\data\\image\\"


class Login_Case(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.browser = self.driver.chrome_browser

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
        self.assertEqual(tip, '林润云收单系统')

    def tearDown(self):
        print("登录测试结束")
        globals()["browser"] = self.browser
        globals()["driver"] = self.driver


class Credit_Case(unittest.TestCase):
    def setUp(self):
        self.driver = globals()["driver"]
        self.browser = globals()["browser"]

    def credit(self):
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "a", "征信进件"))
        div_image = find_element(self.browser, By.CLASS_NAME, "image-field-row")
        image_elements = div_image.find_elements_by_tag_name("label")
        for i in range(0, len(image_elements)):
            self.assertEqual(image_elements[i].text, TestData.credit_image_titles[i])  # 检查上传的图片类型是否缺失
            images = image_elements[i].find_element_by_xpath("./following::*").find_element_by_class_name("image-pane")
            images.click()
            upload_image(path, TestData.credit_image_titles[i])
            while True:
                if "重传" != images.find_element_by_tag_name("button").text:
                    time.sleep(1)
                    if "重传" == images.find_element_by_tag_name("button").text:
                        print("上传完成")
                        break
                else:
                    print("上传完成")
                    break
        div_fields = find_element(self.browser, By.CLASS_NAME, "comp-form-item-fields")
        fields_elements = find_elements_by_element(div_fields, By.TAG_NAME, "label")
        for i in range(0, len(fields_elements) - 2):
            field_name = fields_elements[i].text
            if "姓名" == field_name:
                element_send_key(
                    find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                            By.TAG_NAME, "input"), data.get_userinfo().name)
            elif "身份证号" == field_name:
                element_send_key(
                    find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                            By.TAG_NAME, "input"), data.get_userinfo().idcard)
            elif "手机号" == field_name:
                element_send_key(
                    find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                            By.TAG_NAME, "input"), data.get_userinfo().mobile)
            elif "意向价格" == field_name:
                element_send_key(
                    find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                            By.TAG_NAME, "input"), "200000")
            elif "银行卡号" == field_name:
                element_send_key(
                    find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                            By.TAG_NAME, "input"), data.get_userinfo().bankcode)
            elif "家庭住址" == field_name:
                element_send_key(
                    find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                            By.TAG_NAME, "input"), data.get_userinfo().name + "的家庭住址")
            elif "签发机关" == field_name:
                element_send_key(
                    find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                            By.TAG_NAME, "input"), data.get_userinfo().name + "的发证机关")

        find_element(self.browser, By.CLASS_NAME, "el-checkbox__inner").click()  ##长期有效

    def credit_add_others(self):
        for a in range(1, 4):
            buttons = find_elements(self.browser, By.TAG_NAME, "button")
            if a == 3:
                for i in range(0, len(buttons)):
                    if "新增担保人" == buttons[i].text:
                        element_click(buttons[i])
            else:
                for i in range(0, len(buttons)):
                    if "添加共同还款人" == buttons[i].text:
                        element_click(buttons[i])
            find_element_click(self.browser, By.ID, "tab-" + str(a))
            div_images = find_elements(self.browser, By.CLASS_NAME, "image-field-row")
            image_elements = div_images[a].find_elements_by_tag_name("label")
            for i in range(0, len(image_elements)):
                self.assertEqual(image_elements[i].text, TestData.credit_image_titles[i])  # 检查上传的图片类型是否缺失
                images = image_elements[i].find_element_by_xpath("./following::*").find_element_by_class_name(
                    "image-pane")
                images.click()
                upload_image(path, TestData.credit_image_titles[i])
                while True:
                    if "重传" != images.find_element_by_tag_name("button").text:
                        time.sleep(1)
                        if "重传" == images.find_element_by_tag_name("button").text:
                            print("上传完成")
                            break
                    else:
                        print("上传完成")
                        break
            div_fields = find_elements(self.browser, By.CLASS_NAME, "comp-form-item-fields")
            fields_elements = find_elements_by_element(div_fields[a], By.TAG_NAME, "label")
            for i in range(0, len(fields_elements) - 2):
                field_name = fields_elements[i].text
                if "姓名" == field_name:
                    element_send_key(
                        find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                                By.TAG_NAME, "input"), data.get_userinfo().name)
                elif "身份证号" == field_name:
                    element_send_key(
                        find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                                By.TAG_NAME, "input"), data.get_userinfo().idcard)
                elif "手机号" == field_name:
                    element_send_key(
                        find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                                By.TAG_NAME, "input"), data.get_userinfo().mobile)

                elif "银行卡号" == field_name:
                    element_send_key(
                        find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                                By.TAG_NAME, "input"), data.get_userinfo().bankcode)
                elif "家庭住址" == field_name:
                    element_send_key(
                        find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                                By.TAG_NAME, "input"), data.get_userinfo().name + "的家庭住址")
                elif "签发机关" == field_name:
                    element_send_key(
                        find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                                By.TAG_NAME, "input"), data.get_userinfo().name + "的发证机关")

            find_elements(self.browser, By.CLASS_NAME, "el-checkbox__inner")[a].click()  ##长期有效

    def test_CreditSuccess(self):
        self.credit()
        self.test_CarType0()
        self.test_Bank_E()
        self.credit_add_others()

    def test_CarType0(self):
        cartype = "新车"
        div_fields = find_element(self.browser, By.CLASS_NAME, "comp-form-item-fields")
        fields_elements = find_elements_by_element(div_fields, By.TAG_NAME, "label")
        for i in range(0, len(fields_elements)):
            field_name = fields_elements[i].text
            if "业务类型" == field_name:
                element_click(find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                                      By.TAG_NAME, "input"))
        lis = find_elements(self.browser, By.TAG_NAME, "li")
        for i in range(0, len(lis)):
            if cartype == lis[i].text:
                element_click(lis[i])

    def test_CarType1(self):
        cartype = "二手车"
        div_fields = find_element(self.browser, By.CLASS_NAME, "comp-form-item-fields")
        fields_elements = find_elements_by_element(div_fields, By.TAG_NAME, "label")
        for i in range(0, len(fields_elements)):
            field_name = fields_elements[i].text
            if "业务类型" == field_name:
                element_click(find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                                      By.TAG_NAME, "input"))
        lis = find_elements(self.browser, By.TAG_NAME, "li")
        for i in range(0, len(lis)):
            if cartype == lis[i].text:
                element_click(lis[i])

    def test_Bank_E(self):
        bankname = "济南市胜利街支行"
        div_fields = find_element(self.browser, By.CLASS_NAME, "comp-form-item-fields")
        fields_elements = find_elements_by_element(div_fields, By.TAG_NAME, "label")
        for i in range(0, len(fields_elements)):
            field_name = fields_elements[i].text
            if "贷款银行" == field_name:
                element_click(find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                                      By.TAG_NAME, "input"))
        lis = find_elements(self.browser, By.TAG_NAME, "li")
        for i in range(0, len(lis)):
            if bankname == lis[i].text:
                element_click(lis[i])

    def test_Bank_R(self):
        bankname = "建设银行"
        div_fields = find_element(self.browser, By.CLASS_NAME, "comp-form-item-fields")
        fields_elements = find_elements_by_element(div_fields, By.TAG_NAME, "label")
        for i in range(0, len(fields_elements)):
            field_name = fields_elements[i].text
            if "贷款银行" == field_name:
                element_click(find_element_by_element(find_element_by_element(fields_elements[i], By.XPATH, "./following::*"),
                                                      By.TAG_NAME, "input"))
        lis = find_elements(self.browser, By.TAG_NAME, "li")
        for i in range(0, len(lis)):
            if bankname == lis[i].text:
                element_click(lis[i])

    def tearDown(self):
        buttons = find_elements(self.browser, By.TAG_NAME, "button")
        for i in range(0, len(buttons)):
            if "提交申请" == buttons[i].text:
                element_click(buttons[i])
        div = find_element(self.browser, By.CLASS_NAME, "el-message-box__btns")
        buttons = find_elements_by_element(div, By.TAG_NAME, "button")
        for i in range(0, len(buttons)):
            if "确定" == buttons[i].text:
                element_click(buttons[i])
        print("测试结束")
        # self.driver.tearDown()


if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        print("")
