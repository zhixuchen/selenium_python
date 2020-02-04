#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/15 13:52
# software: PyCharm
from test_case.case import *



class Company_Examine(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.browser = self.driver.chrome_browser
        self.n = 1
        self.log=Logs()
        self.login()
        self.loginbypwd()

    def login(self):
        try:
            data = Data()
            url = data.url
            self.browser.get(url)
        except Exception as e:
            self.log.log_error(e)
            catch_image(self.browser)

    def loginbypwd(self):
        try:
            data = Data()
            account = data.get_account("cs_account")
            pwd = data.get_pwd("cs_pwd")
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(pwd)
            find_elements(self.browser, By.TAG_NAME, "button")[0].click()
        except Exception as e:
            self.log.log_error(e)
            catch_image(self.browser)

    def examine(self):
        tab_stage=find_element(self.browser,By.ID,"tab-stage")
        element_click(tab_stage)
        time.sleep(10)


    def click_selcet_li_by_text(self, text):
        self.n = self.n + 1
        element_div = find_element(self.browser, By.XPATH, "/html/body/div[" + str(self.n) + "]")
        select_element = find_element_by_text_element(element_div, By.TAG_NAME, "li", text)
        element_click(select_element)

    def check_defult(self, check, defult):
        title_div = find_elements(self.browser, By.CLASS_NAME, "lcomp-module-pane")[0]
        title_element = find_element_by_text_element(title_div, By.TAG_NAME, "span", "业务品种")
        car_type = find_next_element(title_element).text
        if check in ["手机号码", "身份证号", "姓名", "证件有效期", "车辆价格"]:
            if "手机号码" == check:
                error_msg = "手机号码为空"
            elif "身份证号" == check:
                error_msg = "身份证号为空"
            elif "姓名" == check:
                error_msg = "姓名为空"
            elif "证件有效期" == check:
                error_msg = "证件有效期为空"
            elif "车辆价格" == check:
                error_msg = "车辆价格为空"
            self.checkIsNotNone(defult, error_msg)
        else:
            if "领卡地区号" == check:
                error_msg = "领卡地区号错误"
                check_value = "10001"
            elif "领卡网点号" == check:
                error_msg = "领卡网点号错误"
                check_value = "10002"
            elif "业务模式" == check:
                error_msg = "业务模式错误"
                check_value = "抵押+合作机构保证(先放款后抵押)"
            elif "自购车状况" == check:
                error_msg = "自购车状况错误"
                check_value = "无"
            elif "卡片领取方式" == check:
                error_msg = "卡片领取方式错误"
                check_value = "自取"
            elif "车架号" == check:
                error_msg = "车架号错误"
                check_value = "00000000000000000"
            elif "收款对象类型" == check:
                error_msg = "收款对象类型错误"
                check_value = "第三方机构"
            elif "抵押品名称" == check:
                error_msg = "抵押品名称错误"
                check_value = "汽车"
            elif "汽车经销商全称" == check:
                error_msg = "汽车经销商全称错误"
                check_value = "山东林润汽车销售服务有限公司"
            elif "分期手续费率" == check:
                error_msg = "分期手续费率错误"
                check_value = "9.5"
            elif "最高抵押率" == check:
                error_msg = "最高抵押率错误"
                if car_type == "新车":
                    check_value = "80"
                elif car_type == "二手车":
                    check_value = "70"
            self.checkEqual(check_value, defult, error_msg)

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
        self.checkEqual(ture_sf_money, sf_money, "首付金额计算有误（首付金额=车辆价格-贷款金额合计）")
        self.checkEqual(true_sf_proportion, sf_proportion, "首付比例计算有误（首付比例=首付金额/车辆价格*100%）")
        self.checkEqual(ture_first_month_money, first_month_money, "首月还款计算有误（首月还款=（贷款金额合计+手续费总额）-月还款金额×（贷款期数-1））")
        self.checkEqual(true_month_money, month_money, "月还款金额计算有误(月还款金额=贷款金额合计/贷款期数+手续费总额/贷款期数)")
        self.checkEqual(true_poundage_amount, poundage_amount, "手续费总额计算有误(手续费总额=贷款金额合计×分期手续费率)")
        self.checkEqual(true_loan_money, loan_money, "贷款金额合计计算有误(贷款金额合计 = 实际贷款额 + 实际贷款额×（总利率 - 分期手续费率）)")
        # self.checkEqual(ture_contract_sf_ratio, contract_sf_ratio, "收入还贷比计算有误(收入还贷比=其他月还款额/还款人月均总收入)")
        self.checkEqual(insureamt, car_price, "车损险投保金额和车辆价格不符")
        self.checkEqual(mortvalue, car_price, "抵押品价值和车辆价格不符")

    def checkEqual(self, first, second, msg):
        try:
            self.assertEqual(first, second, msg=None)
        except Exception as e:
            self.log.log_error(msg)
            catch_image(self.browser)
            self.assertEqual(first, second, msg=None)
            raise

    def checkIsNotNone(self, obj, msg=None):
        try:
            self.assertIsNotNone(obj, msg=None)
        except Exception as e:
            self.log.log_error(msg)
            catch_image(self.browser)
            self.assertIsNotNone(obj, msg=None)
            raise

    def test_Claim(self, car_type):  ##认领操作
        element = find_element(self.browser, By.LINK_TEXT, "用户审核(初审)")
        element_click(element)
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "div", "待认领案件"))
        self.claim_input_car_type(car_type)
        find_elements(self.browser, By.CLASS_NAME, "el-table__row")  # 隐性等待，等待列表元素都展示出来
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "button", "认领"))

    def test_UnClaim(self):  ##退件操作
        element = find_element(self.browser, By.LINK_TEXT, "用户审核(初审)")
        element_click(element)
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "div", "待处理案件"))
        find_elements(self.browser, By.CLASS_NAME, "el-table__row")  # 隐性等待，等待列表元素都展示出来
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "button", "退件"))

    def test_Handle(self, car_type):  ##处理操作
        element = find_element(self.browser, By.LINK_TEXT, "用户审核(初审)")
        element_click(element)
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "div", "待处理案件"))
        self.unclaim_input_car_type(car_type)
        find_elements(self.browser, By.CLASS_NAME, "el-table__row")  # 隐性等待，等待列表元素都展示出来
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "button", "处理"))

    def claim_input_car_type(self, car_type):
        claim_select_div = find_elements(self.browser, By.CLASS_NAME, "comp-form-item-fields")[0]
        select_labels = find_elements_by_element(claim_select_div, By.TAG_NAME, "label")
        for select_label in select_labels:
            if select_label.text == "业务品种":
                input_element = find_next_input_by_element(select_label)
                element_click(input_element)
                self.click_selcet_li_by_text(car_type)
                self.n = 1
        search_button = find_element_by_element(claim_select_div, By.TAG_NAME, "button")
        element_click(search_button)

    def unclaim_input_car_type(self, car_type):
        self.log.log_info(car_type)
        claim_select_div = find_elements(self.browser, By.CLASS_NAME, "comp-form-item-fields")[1]
        select_labels = find_elements_by_element(claim_select_div, By.TAG_NAME, "label")
        for select_label in select_labels:
            if select_label.text == "业务品种":
                input_element = find_next_input_by_element(select_label)
                element_click(input_element)
                element_click(find_element_by_text(self.browser, By.TAG_NAME, "li", car_type))
        search_button = find_element_by_element(claim_select_div, By.TAG_NAME, "button")
        element_click(search_button)

    def examine_text(self,text):
        time.sleep(0.5)
        examine_h5=find_element_by_text(self.browser,By.TAG_NAME,"h4","初审")
        examine_div = find_next_element(examine_h5)
        labels = find_elements_by_element(examine_div, By.TAG_NAME, "label")
        for label in labels:
            if label.text == "审核结果(初审)":
                input_element = find_next_input_by_element(label)
                element_click_script(self.browser,input_element)
                self.click_selcet_li_by_text(text)
                break



    def storage(self):
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "button", "暂存"))

    def submit(self):
        title_div = find_elements(self.browser, By.CLASS_NAME, "lcomp-module-pane")[0]
        title_element = find_element_by_text_element(title_div, By.TAG_NAME, "span", "业务品种")
        car_type = find_next_element(title_element).text
        if car_type == "新车":
            submit_div = find_element(self.browser, By.CLASS_NAME, "fixed-btn-inner")
            element_click(find_element_by_text_element(submit_div, By.TAG_NAME, "button", "提交"))
            self.n = self.n + 1
            element_div = find_element(self.browser, By.XPATH, "/html/body/div[" + str(self.n) + "]")
            element_click(find_element_by_text_element(element_div, By.TAG_NAME, "button", "确定"))
        elif car_type == "二手车":
            submit_div = find_element(self.browser, By.CLASS_NAME, "fixed-btn-inner")
            element_click(find_element_by_text_element(submit_div, By.TAG_NAME, "button", "提交"))
            self.n = self.n + 1
            element_div = find_element(self.browser, By.XPATH, "/html/body/div[" + str(self.n) + "]")
            element_click(find_element_by_text_element(element_div, By.TAG_NAME, "button", "确定"))

            element_div = find_element(self.browser, By.XPATH, "/html/body/div[" + str(self.n) + "]")
            element_click(find_element_by_text_element(element_div, By.TAG_NAME, "button", "确定"))

    def test_ExamineSuccess(self):
        '''分公司初审测试'''
        car_type = "新车"
        text="通过"

        self.test_Handle(car_type)
        self.examine_text(text)
        # self.examine()

        # self.storage()
        self.submit()

    def test_ExamineReject(self):
        '''开卡分期测试'''
        car_type = "二手车"
        text = "拒件"
        self.login()
        self.loginbypwd()
        self.test_Handle(car_type)
        self.examine_text(text)
        # self.examine()

        self.storage()
        # self.submit()

    def test_ExaminePending(self):
        '''开卡分期测试'''
        car_type = "二手车"
        text = "待补件"
        self.login()
        self.loginbypwd()
        self.test_Handle(car_type)
        self.examine_text(text)
        # self.examine()

        self.storage()
        # self.submit()
    def tearDown(self):
        self.log.log_info("开卡_分期测试结束")
        time.sleep(5)
        self.driver.tearDown()
