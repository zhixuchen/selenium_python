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
        self.assertEqual(tip, '林润云系统')

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
        labels = find_elemntsbyelemnt(stage_div, By.TAG_NAME, "label")
        inputs = find_elemntsbyelemnt(stage_div, By.TAG_NAME, "input")

        for label in labels:
            input_element = find_elemntbyelemnt(find_elemntbyelemnt(label, By.XPATH, "./following::*"),
                                                By.TAG_NAME, "input")
            if label.text in ["商品名称", "还款期限"]:  # 必填下拉框
                element_click(input_element)
                if "商品名称" == label.text:
                    element_click(find_elementbytext(self.browser, By.TAG_NAME, "li", "亚琛施耐泽-乘用"))
                    element_click(find_elementbytext(self.browser, By.TAG_NAME, "li", "亚琛施耐泽S5[进口]"))
                    element_click(
                        find_elementbytext(self.browser, By.TAG_NAME, "li", "2012款-AC-Schnitzer-S5-3.0T-A/MT猎鹰版"))
                    element_click(inputs[1])
                    element_click(find_elementbytext(self.browser, By.TAG_NAME, "li", "进口车"))
                elif "还款期限" == label.text:
                    element_click(find_elementbytext(self.browser, By.TAG_NAME, "li", "36 期"))
                    repay_period = input_element.get_attribute("value")

            elif label.text in ["实际贷款额", "总利率", "还款人月均总收入", "其他月还款额", "其他负债余额", "个人总资产"]:  ##必填输入框
                element_click(input_element)
                if "实际贷款额" == label.text:
                    element_send_key(input_element, "200000")
                    contract_loan_money = input_element.get_attribute("value")
                elif "总利率" == label.text:
                    element_send_key(input_element, "25.5")
                    company_service_rate = input_element.get_attribute("value")
                elif "还款人月均总收入" == label.text:
                    element_send_key(input_element, "8000")
                    monthincome = input_element.get_attribute("value")
                elif "其他月还款额" == label.text:
                    element_send_key(input_element, "4200")
                    monrepayamt = input_element.get_attribute("value")
                elif "其他负债余额" == label.text:
                    element_send_key(input_element, "1500000")
                elif "个人总资产" == label.text:
                    element_send_key(input_element, "3000000")
                elif "权属人姓名" == label.text:
                    element_send_key(input_element, data.get_userinfo().name)
            elif label.text in ["现住房面积", "权属人姓名", "关联人月收入"]:  ##页面特殊处理
                self.browser.execute_script("arguments[0].click()", input_element)
                if "现住房面积" == label.text:
                    element_send_key(input_element, "123.8")
                elif "权属人姓名" == label.text:
                    element_send_key(input_element, data.get_userinfo().name)
                elif "关联人月收入" == label.text:
                    element_send_key(input_element, "5000")
            elif label.text in ["发动机号", "他项权证号", "抵押合同编号", "申请人与抵押物权属人关系"]:  # 非必填
                element_click(input_element)
                if "发动机号" == label.text:
                    element_send_key(input_element, "FAGDHJSJKK")

                elif "他项权证号" == label.text:
                    element_send_key(input_element, "FHSKJI00555DA")
                elif "抵押合同编号" == label.text:
                    element_send_key(input_element, "HTLINRUN101211")
                elif "申请人与抵押物权属人关系" == label.text:
                    element_click(find_elementbytext(self.browser, By.TAG_NAME, "li", "本人"))
            elif label.text in ["业务模式", "车架号", "车辆价格", "首付金额", "首付比例", "收入还贷比", "分期手续费率", "首月还款", "月还款金额", "手续费总额",
                                "汽车经销商全称", "最高抵押率", "收款对象类型", "抵押品价值", "车损险投保金额", "贷款金额合计", "抵押品名称"]:
                if label.text in ["业务模式", "车架号", "收款对象类型", "抵押品名称", "汽车经销商全称", "分期手续费率", "最高抵押率"]:
                    defult = input_element.get_attribute("value")
                    self.check_defult(label.text, defult)
                    if label.text == "分期手续费率":
                        commission_fee_rate = defult
                elif label.text in ["车辆价格", "首付金额", "首付比例", "收入还贷比", "首月还款", "月还款金额", "手续费总额", "抵押品价值", "车损险投保金额",
                                    "贷款金额合计"]:
                    if "车辆价格" == label.text:
                        car_price = input_element.get_attribute("value")
                    elif "首付金额" == label.text:
                        sf_money = input_element.get_attribute("value")
                    elif "首付比例" == label.text:
                        sf_proportion = input_element.get_attribute("value")
                    elif "收入还贷比" == label.text:
                        contract_sf_ratio = input_element.get_attribute("value")
                    elif "首月还款" == label.text:
                        first_month_money = input_element.get_attribute("value")
                    elif "月还款金额" == label.text:
                        month_money = input_element.get_attribute("value")
                    elif "手续费总额" == label.text:
                        poundage_amount = input_element.get_attribute("value")
                    elif "抵押品价值" == label.text:
                        mortvalue = input_element.get_attribute("value")
                    elif "车损险投保金额" == label.text:
                        insureamt = input_element.get_attribute("value")
                    elif "贷款金额合计" == label.text:
                        loan_money = input_element.get_attribute("value")
        finance_data = {"car_price": car_price, "sf_money": sf_money, "sf_proportion": sf_proportion,
                        "contract_sf_ratio": contract_sf_ratio, "first_month_money": first_month_money,
                        "month_money": month_money,
                        "poundage_amount": poundage_amount,
                        "insureamt": insureamt, "loan_money": loan_money, "mortvalue": mortvalue,
                        "monthincome": monthincome, "monrepayamt": monrepayamt,
                        "commission_fee_rate": commission_fee_rate,
                        "contract_loan_money": contract_loan_money,
                        "company_service_rate": company_service_rate, "repay_period": repay_period}
        print(finance_data)
        self.check_finance(finance_data)

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
        elif "业务模式" == check:
            self.assertEqual("抵押+合作机构保证(先放款后抵押)", defult)
        elif "车架号" == check:
            self.assertEqual("00000000000000000", defult)
        elif "车辆价格" == check:
            self.assertIsNotNone(defult)
        elif "收款对象类型" == check:
            self.assertEqual("第三方机构", defult)
        elif "抵押品名称" == check:
            self.assertEqual("汽车", defult)

        elif "汽车经销商全称" == check:
            self.assertEqual("山东林润汽车销售服务有限公司", defult)
        elif "分期手续费率" == check:
            self.assertEqual("9.5", defult)
        elif "最高抵押率" == check:
            self.assertEqual("80", defult)

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

    def check_finance(self, finance_data):
        car_price = float(finance_data["car_price"])  # 车辆价格
        loan_money = float(finance_data["loan_money"])  # 贷款金额合计
        sf_money = float(finance_data["sf_money"])  # 首付金额
        sf_proportion = float(finance_data["sf_proportion"])  # 首付比例
        contract_sf_ratio = float(finance_data["contract_sf_ratio"])  # 收入还贷比
        commission_fee_rate = float(finance_data["commission_fee_rate"])  # 分期手续费率
        first_month_money = float(finance_data["first_month_money"])  # 首月还款
        month_money = float(finance_data["month_money"])  # 月还款金额
        poundage_amount = float(finance_data["poundage_amount"])  # 手续费总额
        insureamt = float(finance_data["insureamt"])  # 车损险投保金额
        mortvalue = float(finance_data["mortvalue"])  # 抵押品价值
        repay_period = int(list(filter(str.isdigit, finance_data["repay_period"]))[0] +
                           list(filter(str.isdigit, finance_data["repay_period"]))[1])  # 期数
        monthincome = float(finance_data["monthincome"])  # 还款人月总收入
        monrepayamt = float(finance_data["monrepayamt"])  # 其他月还款额
        company_service_rate = float(finance_data["company_service_rate"])  # 总利率
        contract_loan_money = float(finance_data["contract_loan_money"])  # 实际贷款额
        true_sf_proportion = round(100 * (sf_money / car_price), 2)
        ture_sf_money = round(car_price - loan_money)
        ture_contract_sf_ratio = (monrepayamt / monthincome) * 100  # 百分比
        ture_first_month_money = round((loan_money + poundage_amount) - month_money * (repay_period - 1))
        true_month_money = int(loan_money / repay_period) + int(poundage_amount / repay_period)  ##两个取整相加
        true_poundage_amount = round((loan_money * commission_fee_rate) / 100)
        true_loan_money = int(math.ceil((contract_loan_money + contract_loan_money * (
                    company_service_rate - commission_fee_rate) / 100) / 100)) * 100  # 取百
        self.assertEqual(ture_sf_money, sf_money, "首付金额计算有误（首付金额=车辆价格-贷款金额合计）")
        self.assertEqual(true_sf_proportion, sf_proportion, "首付比例计算有误（首付比例=首付金额/车辆价格*100%）")
        self.assertEqual(ture_first_month_money, first_month_money, "首月还款计算有误（首月还款=（贷款金额合计+手续费总额）-月还款金额×（贷款期数-1））")
        self.assertEqual(true_month_money, month_money, "月还款金额计算有误(月还款金额=贷款金额合计/贷款期数+手续费总额/贷款期数)")
        self.assertEqual(true_poundage_amount, poundage_amount, "手续费总额计算有误(手续费总额=贷款金额合计×分期手续费率)")
        self.assertEqual(true_loan_money, loan_money, "贷款金额合计计算有误(贷款金额合计 = 实际贷款额 + 实际贷款额×（总利率 - 分期手续费率）)")
        self.assertEqual(ture_contract_sf_ratio, contract_sf_ratio, "收入还贷比计算有误(收入还贷比=其他月还款额/还款人月均总收入)")
        self.assertEqual(insureamt, car_price, "车损险投保金额和车辆价格不符")
        self.assertEqual(mortvalue, car_price, "抵押品价值和车辆价格不符")

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

        element_click(find_elementbytext(self.browser, By.TAG_NAME, "button", "暂存"))

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
