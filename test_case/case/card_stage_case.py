#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/15 13:52
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
            account = data.get_account("kk_account")
            pwd = data.get_pwd("kk_pwd")
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


class Card_Case(unittest.TestCase):
    def setUp(self):
        self.driver = globals()["driver"]
        self.browser = globals()["browser"]

    def card(self):
        print("开始处理开卡")
        # find_element_click(self.browser,By.ID,"tab-card")
        card_div = find_element(self.browser, By.ID, "pane-card")
        labels = find_elemntsbyelemnt(card_div, By.TAG_NAME, "label")
        for label in labels:

            if label.text in ["婚姻状况", "受教育程度", "住宅状况", "职务", "单位性质", "与开卡人关系", "职业及职级"]:
                if "婚姻状况" == label.text:
                    element_click(find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                      By.TAG_NAME, "input"))
                    select_element = find_elementbytext(self.browser, By.TAG_NAME, "li", "未婚(无配偶)")
                    element_click(select_element)


                elif "受教育程度" == label.text:
                    element_click(find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                      By.TAG_NAME, "input"))
                    select_element = find_elementbytext(self.browser, By.TAG_NAME, "li", "博士及以上")
                    element_click(select_element)
                elif "住宅状况" == label.text:
                    element_click(find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                      By.TAG_NAME, "input"))
                    select_element = find_elementbytext(self.browser, By.TAG_NAME, "li", "自有住房")
                    element_click(select_element)

                elif "职务" == label.text:
                    element_click(find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                      By.TAG_NAME, "input"))
                    select_element = find_elementbytext(self.browser, By.TAG_NAME, "li", "部、省级、副部、副省级")
                    element_click(select_element)


                elif "单位性质" == label.text:
                    element_click(find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                      By.TAG_NAME, "input"))

                    select_element = find_elementbytext(self.browser, By.TAG_NAME, "li", "国有")
                    element_click(select_element)

                elif "职业及职级" == label.text:
                    element = find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                  By.TAG_NAME, "input")
                    self.browser.execute_script("arguments[0].click()", element)

                    select_element = find_elementbytext(self.browser, By.TAG_NAME, "li", "公务员")
                    element_click(select_element)


                elif "与开卡人关系" == label.text:
                    element_click(find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                      By.TAG_NAME, "input"))

                    select_element = find_elementbytext(self.browser, By.TAG_NAME, "li", "父子")
                    element_click(select_element)

            elif label.text in ["住宅邮编", "住宅详细地址", "单位名称", "单位邮编", "详细地址", "联系人姓名", "联系人手机"]:
                element_send_key(
                    find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                        By.TAG_NAME, "input"), label.text)
                if "联系人手机" == label.text:
                    element_send_key(
                        find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                            By.TAG_NAME, "input"), data.user_info.mobile)

            elif label.text in ["手机号码", "自购车状况", "卡片领取方式", "领卡地区号", "领卡网点号", "身份证号", "姓名", "证件有效期"]:
                defult = find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                             By.TAG_NAME, "input").get_attribute('value')
                try:
                    self.check_defult(label.text, defult)
                except Exception as e:
                    print("断言校验错误：" + e)

            elif label.text in ["住宅地址", "何时入住", "单位电话", "单位地址", "何时入职", "联系人电话"]:

                if label.text in ["住宅地址", "单位地址"]:

                    element = find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                  By.TAG_NAME, "input")
                    self.browser.execute_script("arguments[0].click()", element)
                    select_s_element = find_elementbytext(self.browser, By.TAG_NAME, "li", "浙江省")
                    element_click(select_s_element)
                    select_c_element = find_elementbytext(self.browser, By.TAG_NAME, "li", "杭州市")
                    element_click(select_c_element)
                    select_q_element = find_elementbytext(self.browser, By.TAG_NAME, "li", "西湖区")
                    element_click(select_q_element)

                elif label.text in ["何时入住", "何时入职"]:
                    time_element = find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                       By.TAG_NAME, "input")
                    if label.text == "何时入住":
                        element_send_key(time_element, "2019-01-05")
                    elif label.text == "何时入职":
                        element_send_key(time_element, "201801")

                if label.text in ["单位电话", "联系人电话"]:
                    area_element = find_elemntsbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                        By.TAG_NAME, "input")[0]
                    area_element.send_keys("0577")
                    mobile_element = find_elemntsbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                          By.TAG_NAME, "input")[1]
                    mobile_element.click()
                    mobile_element = find_elemntsbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                          By.TAG_NAME, "input")[1]
                    mobile_element.send_keys("63891171")

            # if label.text in ["婚姻状况", "受教育程度", "住宅状况", "职务", "单位性质", "与开卡人关系", "职业及职级", "自购车状况", "卡片领取方式"]:
            #     try:
            #         self.check_select(label.text,select_element)
            #     except Exception as e:
            #         print("校验下拉选项出错：" + e)

    def stage(self):
        print("开始处理分期信息")
        time.sleep(2)
        find_element_click(self.browser, By.ID, "tab-stage")
        stage_div = find_element(self.browser, By.ID, "pane-stage")

    def check_defult(self, check, defult):
        if "领卡地区号" == check:
            self.assertEqual("10001", defult)
        elif "领卡网点号" == check:
            self.assertEqual("10002", defult)
        elif "手机号码" == check:
            self.assertEqual(11, len(defult))
        elif "自购车状况" == check:
            self.assertEqual("无", defult)
        elif "卡片领取方式" == check:
            self.assertEqual("自取", defult)
        elif "身份证号" == check:
            self.assertEqual(18, len(defult))
        elif "姓名" == check:
            self.assertIsNotNone(defult)
        elif "证件有效期" == check:
            self.assertIsNotNone(defult)

    def check_select(self, check, select_element):
        if "婚姻状况" == check:
            lis = find_elemntsbyelemnt(
                find_elemntbyelemnt(select_element, By.XPATH, ".."),
                By.TAG_NAME, "li")
            self.assertEqual("未婚(无配偶)", lis[0].text)
            self.assertEqual("已婚(有配偶)", lis[1].text)
            self.assertEqual("分居", lis[2].text)
            self.assertEqual("离异", lis[3].text)
            self.assertEqual("丧偶", lis[4].text)
            self.assertEqual("其他", lis[5].text)
        elif "受教育程度" == check:
            lis = find_elemntsbyelemnt(
                find_elemntbyelemnt(select_element, By.XPATH, ".."),
                By.TAG_NAME, "li")
            self.assertEqual("博士及以上", lis[0].text)
            self.assertEqual("硕士研究生", lis[1].text)
            self.assertEqual("大学本科", lis[2].text)
            self.assertEqual("大学专科/电大", lis[3].text)
            self.assertEqual("中专", lis[4].text)
            self.assertEqual("技工学校", lis[5].text)
            self.assertEqual("高中", lis[6].text)
            self.assertEqual("初中", lis[7].text)
            self.assertEqual("小学及以下", lis[8].text)
        elif "住宅状况" == check:
            lis = find_elemntsbyelemnt(
                find_elemntbyelemnt(select_element, By.XPATH, ".."),
                By.TAG_NAME, "li")
            self.assertEqual("自有住房", lis[0].text)
            self.assertEqual("分期付款购房", lis[1].text)
            self.assertEqual("租房", lis[2].text)
            self.assertEqual("其他", lis[3].text)
            self.assertEqual("集体宿舍", lis[4].text)
            self.assertEqual("单位分配", lis[5].text)
        elif "职务" == check:
            lis = find_elemntsbyelemnt(
                find_elemntbyelemnt(select_element, By.XPATH, ".."),
                By.TAG_NAME, "li")
            self.assertEqual("部、省级、副部、副省级", lis[0].text)
            self.assertEqual("董事/司、局、地、厅级", lis[1].text)
            self.assertEqual("总经理/县处级", lis[2].text)
            self.assertEqual("科级/部门经理", lis[3].text)
            self.assertEqual("职员/科员级", lis[4].text)
        elif "单位性质" == check:
            lis = find_elemntsbyelemnt(
                find_elemntbyelemnt(select_element, By.XPATH, ".."),
                By.TAG_NAME, "li")
            print(len(lis))
            for i in range(0, len(lis)):
                time.sleep(0.1)
                print("lis" + str(i) + ":" + lis[i].text)
            self.assertEqual("国有", lis[0].text)
            self.assertEqual("集体", lis[1].text)
            self.assertEqual("国有控股", lis[2].text)
            self.assertEqual("集体控股", lis[3].text)
            self.assertEqual("三资", lis[4].text)
            self.assertEqual("私营", lis[5].text)
            self.assertEqual("个体", lis[6].text)
            self.assertEqual("外贸", lis[7].text)
            self.assertEqual("股份合作", lis[8].text)
            self.assertEqual("其他股份制", lis[9].text)
            self.assertEqual("民营", lis[10].text)
            self.assertEqual("联营", lis[11].text)
            self.assertEqual("乡镇企业", lis[12].text)
            self.assertEqual("其他", lis[13].text)
        elif "职业及职级" == check:
            lis = find_elemntsbyelemnt(
                find_elemntbyelemnt(select_element, By.XPATH, ".."),
                By.TAG_NAME, "li")
            self.assertEqual("公务员", lis[0].text)
            self.assertEqual("事业单位员工", lis[1].text)
            self.assertEqual("职员", lis[2].text)
            self.assertEqual("军人", lis[3].text)
            self.assertEqual("自由职业者", lis[4].text)
            self.assertEqual("工人", lis[5].text)
            self.assertEqual("农民", lis[6].text)
            self.assertEqual("邮电通讯行业职员", lis[7].text)
            self.assertEqual("房地产行业职员", lis[8].text)
            self.assertEqual("交通运输行业职员", lis[9].text)
            self.assertEqual("法律/司法行业职员", lis[10].text)
            self.assertEqual("文化/娱乐/体育行业职员", lis[11].text)
            self.assertEqual("媒介/广告行业职员", lis[12].text)
            self.assertEqual("科研/教育行业职员", lis[13].text)
            self.assertEqual("学生", lis[14].text)
            self.assertEqual("计算机/网络行业职员", lis[15].text)
            self.assertEqual("商业贸易行业职员", lis[16].text)
            self.assertEqual("银行/金融/证券/投资行业职员", lis[17].text)
            self.assertEqual("税务行业职员", lis[18].text)
            self.assertEqual("咨询行业职员", lis[19].text)
            self.assertEqual("社会服务行业职员", lis[20].text)
            self.assertEqual("旅游/饭店行业职员", lis[21].text)
            self.assertEqual("健康/医疗服务行业职员", lis[22].text)
            self.assertEqual("管理人员", lis[23].text)
            self.assertEqual("技术人员", lis[24].text)
            self.assertEqual("文体明星", lis[25].text)
            self.assertEqual("无职业", lis[26].text)
            self.assertEqual("私人业主", lis[27].text)
        elif "自购车状况" == check:
            lis = find_elemntsbyelemnt(
                find_elemntbyelemnt(find_elementbytext(self.browser, By.TAG_NAME, "li", "有"), By.XPATH, ".."),
                By.TAG_NAME, "li")
            self.assertEqual("有", lis[0].text)
            self.assertEqual("无", lis[1].text)
        elif "与开卡人关系" == check:
            lis = find_elemntsbyelemnt(
                find_elemntbyelemnt(select_element, By.XPATH, ".."),
                By.TAG_NAME, "li")
            self.assertEqual("父子", lis[0].text)
            self.assertEqual("母子", lis[1].text)
            self.assertEqual("兄弟姐妹", lis[2].text)
            self.assertEqual("亲属", lis[3].text)
            self.assertEqual("夫妻", lis[4].text)
            self.assertEqual("同学", lis[5].text)
            self.assertEqual("同乡", lis[6].text)
            self.assertEqual("朋友", lis[7].text)
            self.assertEqual("同事", lis[8].text)
        elif "卡片领取方式" == check:
            lis = find_elemntsbyelemnt(
                find_elemntbyelemnt(select_element, By.XPATH, ".."),
                By.TAG_NAME, "li")
            self.assertEqual("自取", lis[0].text)
            self.assertEqual("寄送单位地址", lis[1].text)
            self.assertEqual("寄送住宅地址", lis[2].text)

    def test_Claim(self):  ##认领操作
        element_click(find_elementbytext(self.browser, By.TAG_NAME, "a", "开卡分期列表"))
        element_click(find_elementbytext(self.browser, By.TAG_NAME, "div", "待认领案件"))
        find_elements(self.browser, By.CLASS_NAME, "el-table__row")  # 隐性等待，等待列表元素都展示出来
        element_click(find_elementbytext(self.browser, By.TAG_NAME, "button", "认领"))

    def test_UnClaim(self):  ##退件操作
        element_click(find_elementbytext(self.browser, By.TAG_NAME, "a", "开卡分期列表"))
        element_click(find_elementbytext(self.browser, By.TAG_NAME, "div", "待处理案件"))
        find_elements(self.browser, By.CLASS_NAME, "el-table__row")  # 隐性等待，等待列表元素都展示出来
        element_click(find_elementbytext(self.browser, By.TAG_NAME, "button", "退件"))

    def test_Handle(self):  ##处理操作
        element_click(find_elementbytext(self.browser, By.TAG_NAME, "a", "开卡分期列表"))
        element_click(find_elementbytext(self.browser, By.TAG_NAME, "div", "待处理案件"))
        find_elements(self.browser, By.CLASS_NAME, "el-table__row")  # 隐性等待，等待列表元素都展示出来
        element_click(find_elementbytext(self.browser, By.TAG_NAME, "button", "处理"))

    def storage(self):

        element_click(find_elementbytext(self.browser,By.TAG_NAME,"button","暂存"))


    def submit(self):

        element_click(find_elementbytext(self.browser, By.TAG_NAME, "button", "提交"))
    def test_CardSuccess(self):
        self.test_Handle()
        # self.card()
        self.stage()
        # self.storage()
        # self.submit()

    def tearDown(self):
        print("开卡测试结束")


if __name__ == '__main__':
    try:
        print("")
    except Exception as e:
        print("")
