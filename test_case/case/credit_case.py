#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/13 12:14
# software: PyCharm
from test_case.case import *

root_path = os.path.abspath(os.path.dirname(__file__)).split('selenium_python')[0]
path = root_path + "selenium_python\\test_case\\data\\image\\"


class Credit_Case(unittest.TestCase):
    def setUp(self):
        self.data = Data()
        self.TestData = Test_Data()
        self.n = 1
        self.driver = Driver()
        self.browser = self.driver.chrome_browser
        self.log = Logs()
        self.image = Image()  ## 初始化截屏功能
        self.login()
        self.loginbypwd()


    def login(self):
        try:
            url = self.data.url
            self.browser.get(url)
        except Exception as e:
            self.log.log_error(e)
            self.image.catch_image(self.browser)

    def loginbypwd(self):
        try:
            account = self.data.get_account("xs_account")
            pwd = self.data.get_pwd("xs_pwd")
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(pwd)
            find_elements(self.browser, By.TAG_NAME, "button")[0].click()
        except Exception as e:
            self.log.log_error(e)
            self.image.catch_image(self.browser)

    def credit(self):
        element = find_element(self.browser, By.LINK_TEXT, "征信进件")
        element_click(element)
        div_image = find_element(self.browser, By.CLASS_NAME, "image-field-row")
        image_elements = find_elements_by_element(div_image, By.TAG_NAME, "label")
        self.image(image_elements)
        div_fields = find_element(self.browser, By.CLASS_NAME, "comp-form-item-fields")
        titles = ["姓名", "身份证号", "手机号", "意向价格", "银行卡号", "家庭住址", "签发机关"]
        for title in titles:
            if "姓名" == title:
                key = self.data.get_userinfo().name
            elif "身份证号" == title:
                key = self.data.get_userinfo().idcard
            elif "手机号" == title:
                key = self.data.get_userinfo().mobile
            elif "意向价格" == title:
                key = "200000"
            elif "银行卡号" == title:
                key = self.data.get_userinfo().bankcode
            elif "家庭住址" == title:
                key = self.data.get_userinfo().name + "的家庭住址"
            elif "签发机关" == title:
                key = self.data.get_userinfo().name + "的发证机关"
            send_key_by_input_title(div_fields, title, key)

    def credit_add_others(self):
        for a in range(1, 4):
            action_button_div = find_element(self.browser, By.CLASS_NAME, "action-btns")
            buttons = find_elements_by_element(action_button_div, By.TAG_NAME, "button")
            if a == 3:
                for i in range(0, len(buttons)):
                    if "新增担保人" == buttons[i].text:
                        element_click(buttons[i])
                        break
            else:
                for i in range(0, len(buttons)):
                    if "添加共同还款人" == buttons[i].text:
                        element_click(buttons[i])
                        break
            element = find_element(self.browser, By.ID, "tab-" + str(a))
            element_click(element)
            div_images = find_elements(self.browser, By.CLASS_NAME, "image-field-row")
            image_elements = find_elements_by_element(div_images[a], By.TAG_NAME, "label")
            self.image(image_elements)
            div_fields = find_elements(self.browser, By.CLASS_NAME, "comp-form-item-fields")
            titles = ["姓名", "身份证号", "手机号", "银行卡号", "家庭住址", "签发机关"]
            for title in titles:
                if "姓名" == title:
                    key = self.data.get_userinfo().name
                elif "身份证号" == title:
                    key = self.data.get_userinfo().idcard
                elif "手机号" == title:
                    key = self.data.get_userinfo().mobile
                elif "银行卡号" == title:
                    key = self.data.get_userinfo().bankcode
                elif "家庭住址" == title:
                    key = self.data.get_userinfo().name + "的家庭住址"
                elif "签发机关" == title:
                    key = self.data.get_userinfo().name + "的发证机关"
                send_key_by_input_title(div_fields[a], title, key)
            find_elements(self.browser, By.CLASS_NAME, "el-checkbox__inner")[a].click()  ##长期有效

    def image(self, image_elements):
        for i in range(0, len(image_elements)):
            self.check_Equal(image_elements[i].text, self.TestData.credit_image_titles[i])  # 检查上传的图片类型是否缺失
            images = find_element_by_element(find_next_element(image_elements[i]), By.CLASS_NAME, "image-pane")
            element_click(images)
            upload_image(path, self.TestData.credit_image_titles[i])
            sleep_time = 1
            while True:
                if "重传" != find_element_by_element(images, By.TAG_NAME, "button").text:
                    time.sleep(1)
                    sleep_time = sleep_time + 1
                    self.log.log_info("等待上传成功。。。。")
                    if "重传" == find_element_by_element(images, By.TAG_NAME, "button").text:
                        break
                    elif sleep_time > 10:
                        self.log.log_info("等待超过10秒，不继续等待")
                        break
                else:
                    break

    def click_selcet_li_by_text(self, text):
        self.n = self.n + 1
        element_div = find_element(self.browser, By.XPATH, "/html/body/div[" + str(self.n) + "]")
        select_element = find_element_by_text_element(element_div, By.TAG_NAME, "li", text)
        element_click(select_element)

    def select_CarTyp(self, cartype):

        div_fields = find_element(self.browser, By.CLASS_NAME, "comp-form-item-fields")
        fields_elements = find_elements_by_element(div_fields, By.TAG_NAME, "label")
        for i in range(0, len(fields_elements)):
            field_name = fields_elements[i].text
            if "业务类型" == field_name:
                element_click(
                    find_next_input_by_element(fields_elements[i]))
                break
        self.click_selcet_li_by_text(cartype)

    def select_Bank(self, bankname):
        div_fields = find_element(self.browser, By.CLASS_NAME, "comp-form-item-fields")
        fields_elements = find_elements_by_element(div_fields, By.TAG_NAME, "label")
        for i in range(0, len(fields_elements)):
            field_name = fields_elements[i].text
            if "贷款银行" == field_name:
                element_click(
                    find_next_input_by_element(fields_elements[i]))
                break
        self.click_selcet_li_by_text(bankname)

    def select_time(self):
        element_send_key(find_elements(self.browser, By.CLASS_NAME, "el-range-input")[0], "2018-01-01")
        element_send_key(find_elements(self.browser, By.CLASS_NAME, "el-range-input")[1], "2030-01-01")

    def check_Equal(self, first, second, msg=None):
        try:
            self.assertEqual(first, second, msg=None)
        except AssertionError:
            self.image.catch_image(self.browser)
            raise

    def submit(self):
        buttons = find_elements(self.browser, By.TAG_NAME, "button")
        for i in range(0, len(buttons)):
            if "提交申请" == buttons[i].text:
                element_click(buttons[i])
        div = find_element(self.browser, By.CLASS_NAME, "el-message-box__btns")
        buttons = find_elements_by_element(div, By.TAG_NAME, "button")
        for i in range(0, len(buttons)):
            if "确定" == buttons[i].text:
                element_click(buttons[i])
        success_tip = find_element(self.browser, By.CLASS_NAME, "el-message__content").text

        self.check_Equal(success_tip, '提交成功')

    def test_E_X_Credit(self):
        '''E分期银行新车-ouy'''
        cartype = "新车"
        bankname = "济南市胜利街支行"
        self.credit()
        self.select_CarTyp(cartype)
        self.select_Bank(bankname)
        self.select_time()
        self.credit_add_others()
        self.submit()

    def test_E_E_Credit(self):
        '''E分期银行二手车-niu'''
        cartype = "二手车"
        bankname = "济南市胜利街支行"
        self.credit()
        self.select_CarTyp(cartype)
        self.select_Bank(bankname)
        self.select_time()
        self.credit_add_others()
        self.submit()

    def tearDown(self):
        self.log.log_info("测试结束")
        time.sleep(3)
        self.driver.tearDown()
