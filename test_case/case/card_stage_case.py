#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/15 13:52
# software: PyCharm
from test_case.case import *

class Card_Case(unittest.TestCase):
    def setUp(self):##初始化
        self.driver = Driver() ##初始化浏览器驱动
        self.browser = self.driver.chrome_browser ##启动谷歌驱动
        self.n = 1 ##设置全局变量n，初始默认为1
        self.log = Logs() ##初始化日志类
        self.data = Data()  ##初始化测试数据类
        self.login()  ## 打开登录页面
        self.loginbypwd() ## 通过密码登录

    def login(self):## 打开登录页面
        try:
            self.data = Data()
            url = self.data.url
            self.browser.get(url)
        except Exception as e:
            self.log.log_error(e)
            catch_image(self.browser)

    def loginbypwd(self): ## 通过密码登录
        try:
            account = self.data.get_account("kk_account")
            pwd = self.data.get_pwd("kk_pwd")
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[0].send_keys(account)
            find_elements(self.browser, By.CLASS_NAME, "el-input__inner")[1].send_keys(pwd)
            find_elements(self.browser, By.TAG_NAME, "button")[0].click()
        except Exception as e:
            self.log.log_error(e)
            catch_image(self.browser)

    def card(self):
        '''开卡测试'''
        try:
            card_div = find_element(self.browser, By.ID, "pane-card")
            labels = find_elements_by_element(card_div, By.TAG_NAME, "label")
        except Exception as e:
            self.log.log_error("执行用例失败：" + e)
        check_list = ["婚姻状况", "受教育程度", "住宅状况", "职务", "单位性质", "与开卡人关系", "职业及职级", "自购车状况", "卡片领取方式"]
        select_div = find_elements(self.browser, By.CLASS_NAME, "comp-form-item-fields")[0]
        self.check_select_list(check_list, select_div)
        self.log.log_info("开卡页面下拉框选项校验通过")
        for label in labels:
            try:
                input_element = find_next_input_by_element(label)
                if label.text in ["婚姻状况", "受教育程度", "住宅状况", "职务",  "与开卡人关系"]:
                    element_click(input_element)
                    if "婚姻状况" == label.text:
                        self.click_selcet_li_by_text("未婚(无配偶)")
                    elif "受教育程度" == label.text:
                        self.click_selcet_li_by_text("博士及以上")
                    elif "住宅状况" == label.text:
                        self.click_selcet_li_by_text("自有住房")
                    elif "职务" == label.text:
                        self.click_selcet_li_by_text("部、省级、副部、副省级")
                    elif "与开卡人关系" == label.text:
                        self.click_selcet_li_by_text("父子")
                elif label.text in ["住宅邮编", "住宅详细地址", "单位名称", "单位邮编", "详细地址", "联系人姓名", "联系人手机"]:
                    element_send_key(input_element, label.text)
                    if "联系人手机" == label.text:
                        element_send_key(input_element, self.data.get_userinfo().mobile)
                elif label.text in ["住宅地址", "何时入住", "单位电话", "单位地址", "何时入职", "联系人电话", "职业及职级","单位性质"]:
                    element = input_element
                    if label.text in ["住宅地址", "单位地址"]:
                        self.n = self.n + 1
                        element_click_script(self.browser, element)
                        live_element_div = find_element(self.browser, By.XPATH, "/html/body/div[" + str(self.n) + "]")
                        sheng_element_ul = find_elements_by_element(live_element_div, By.TAG_NAME, "ul")[0]
                        select_s_element = find_element_by_text_element(sheng_element_ul, By.TAG_NAME, "li", "浙江省")
                        element_click(select_s_element)
                        shi_element_ul = find_elements_by_element(live_element_div, By.TAG_NAME, "ul")[1]
                        select_c_element = find_element_by_text_element(shi_element_ul, By.TAG_NAME, "li", "杭州市")
                        element_click(select_c_element)
                        qu_element_ul = find_elements_by_element(live_element_div, By.TAG_NAME, "ul")[2]
                        select_q_element = find_element_by_text_element(qu_element_ul, By.TAG_NAME, "li", "西湖区")
                        element_click(select_q_element)
                    elif "职业及职级" == label.text:
                        element_click_script(self.browser, element)
                        self.click_selcet_li_by_text("公务员")
                    elif "单位性质" == label.text:
                        element_click_script(self.browser, element)
                        self.click_selcet_li_by_text("国有")
                    elif label.text in ["何时入住", "何时入职"]:
                        if label.text == "何时入住":
                            element_send_key(element, "2019-01-05")
                        elif label.text == "何时入职":
                            element_send_key(element, "201801")
                    if label.text in ["单位电话", "联系人电话"]:
                        area_element = find_next_inputs_by_element(label)[0]
                        element_send_key(area_element,"0577")
                        mobile_element = find_next_inputs_by_element(label)[1]
                        element_click(mobile_element)
                        mobile_element = find_next_inputs_by_element(label)[1]
                        element_send_key(mobile_element,"63891171")
            except Exception as e:
                self.log.log_error("执行用例失败：" + e)
            if label.text in ["手机号码", "自购车状况", "卡片领取方式", "领卡地区号", "领卡网点号", "身份证号", "姓名", "证件有效期"]:
                defult = input_element.get_attribute('value')
                self.check_defult(label.text, defult)
        self.log.log_info("开卡页面默认值校验通过")


    def stage(self):
        '''分期信息测试'''
        try:
            tab_element = find_element(self.browser, By.ID, "tab-stage")
            element_click(tab_element)
        except Exception as e:
            self.log.log_error("执行用例报错：" + e)
        check_list = ["业务模式", "还款期限", "申请人与抵押物权属人关系", "收款对象类型"]
        select_div = find_elements(self.browser, By.CLASS_NAME, "comp-form-item-fields")[1]
        self.check_select_list(check_list, select_div)
        self.log.log_info("分期页面下拉框选项校验通过")
        try:
            stage_div = find_element(self.browser, By.ID, "pane-stage")
            labels = find_elements_by_element(stage_div, By.TAG_NAME, "label")
            inputs = find_elements_by_element(stage_div, By.TAG_NAME, "input")
            for label in labels:
                input_element = find_next_input_by_element(label)
                if label.text in ["商品名称", "还款期限"]:  # 必填下拉框
                    element_click(input_element)
                    if "商品名称" == label.text:
                        car_div = find_element(self.browser, By.CLASS_NAME, "cascader-panel")
                        car_first_div = find_element_by_element(car_div, By.CSS_SELECTOR,
                                                                "[class='cascader-content top-menu']")
                        element_click(find_element_by_text_element(car_first_div, By.TAG_NAME, "li", "亚琛施耐泽-乘用"))
                        car_sencond_div = find_element_by_element(car_div, By.CSS_SELECTOR,
                                                                  "[class='cascader-content second-menu']")
                        element_click(find_element_by_text_element(car_sencond_div, By.TAG_NAME, "li", "亚琛施耐泽S5[进口]"))
                        car_last_div = find_element_by_element(car_div, By.CSS_SELECTOR,
                                                               "[class='cascader-content last-menu']")
                        element_click(
                            find_element_by_text_element(car_last_div, By.TAG_NAME, "li",
                                                         "2012款-AC-Schnitzer-S5-3.0T-A/MT猎鹰版"))
                        element_click(inputs[1])
                        self.click_selcet_li_by_text("进口车")
                    elif "还款期限" == label.text:
                        self.click_selcet_li_by_text("36 期")
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
                        element_send_key(input_element, self.data.get_userinfo().name)
                elif label.text in ["现住房面积", "权属人姓名", "关联人月收入", "抵押合同编号"]:  ##页面特殊处理
                    self.browser.execute_script("arguments[0].click()", input_element)
                    if "现住房面积" == label.text:
                        element_send_key(input_element, "123.8")
                    elif "权属人姓名" == label.text:
                        element_send_key(input_element, self.data.get_userinfo().name)
                    elif "关联人月收入" == label.text:
                        element_send_key(input_element, "5000")
                    elif "抵押合同编号" == label.text:
                        element_send_key(input_element, "HTLINRUN101211")
                elif label.text in ["发动机号", "他项权证号", "申请人与抵押物权属人关系"]:  # 非必填
                    element_click(input_element)
                    if "发动机号" == label.text:
                        element_send_key(input_element, "FAGDHJSJKK")
                    elif "他项权证号" == label.text:
                        element_send_key(input_element, "FHSKJI00555DA")
                    elif "申请人与抵押物权属人关系" == label.text:
                        self.click_selcet_li_by_text("本人")
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

        except Exception as e:
            self.log.log_error("执行用例报错：" + e)
        self.log.log_info("分期页面默认值校验通过")
        self.check_finance(finance_data)
        self.log.log_info("分期页面金额计算校验通过")

    def click_selcet_li_by_text(self, text):##点击下拉选择项
        self.n = self.n + 1
        element_div = find_element(self.browser, By.XPATH, "/html/body/div[" + str(self.n) + "]")
        select_element = find_element_by_text_element(element_div, By.TAG_NAME, "li", text)
        element_click(select_element)

    def check_defult(self, check, defult): ##检验默认值
        title_div = find_elements(self.browser, By.CLASS_NAME, "lcomp-module-pane")[0]
        title_element = find_element_by_text_element(title_div, By.TAG_NAME, "span", "业务品种")
        car_type = find_next_element(title_element).text
        if check in ["手机号码", "身份证号", "姓名", "证件有效期", "车辆价格"]:
            self.checkIsNotNone(defult)
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
            self.check_Equal(check_value, defult, error_msg)

    def check_select_list(self, check_list, select_div): ##检验下拉框内的值是否显示完整
        for check in check_list:
            label = find_element_by_text_element(select_div, By.TAG_NAME, "label", check)
            next_div = find_next_element(label)
            ul = find_element_by_element(next_div, By.TAG_NAME, "ul")
            lis = find_elements_by_element(ul, By.TAG_NAME, "li")
            if "婚姻状况" == check:
                true_list = ["未婚(无配偶)", "已婚(有配偶)", "分居", "离异", "丧偶", "其他"]
            elif "受教育程度" == check:
                true_list = ["博士及以上", "硕士研究生", "大学本科", "大学专科/电大", "中专", "技工学校", "高中", "初中", "小学及以下"]
            elif "住宅状况" == check:
                true_list = ["自有住房", "分期付款购房", "租房", "其他", "集体宿舍", "单位分配", ]
            elif "职务" == check:
                true_list = ["部、省级、副部、副省级", "董事/司、局、地、厅级", "总经理/县处级", "科级/部门经理", "职员/科员级"]
            elif "单位性质" == check:
                true_list = ["国有", "集体", "国有控股", "集体控股", "三资", "私营", "个体", "外贸", "股份合作", "其他股份制", "民营", "联营", "乡镇企业",
                             "其他"]
            elif "职业及职级" == check:
                true_list = ["公务员", "事业单位员工", "职员", "军人", "自由职业者", "工人", "农民", "邮电通讯行业职员", "房地产行业职员", "交通运输行业职员",
                             "法律/司法行业职员", "文化/娱乐/体育行业职员", "媒介/广告行业职员", "科研/教育行业职员", "学生", "计算机/网络行业职员", "商业贸易行业职员",
                             "银行/金融/证券/投资行业职员", "税务行业职员", "咨询行业职员", "社会服务行业职员", "旅游/饭店行业职员", "健康/医疗服务行业职员", "管理人员",
                             "技术人员", "文体明星", "无职业", "私人业主"]
            elif "自购车状况" == check:
                true_list = ["有", "无", ]
            elif "与开卡人关系" == check:
                true_list = ["父子", "母子", "兄弟姐妹", "亲属", "夫妻", "同学", "同乡", "朋友", "同事"]
            elif "卡片领取方式" == check:
                true_list = ["自取", "寄送单位地址", "寄送住宅地址"]
            elif "业务模式" == check:
                true_list = ["抵押+合作机构保证(先放款后抵押)"]
            elif "还款期限" == check:
                true_list = ["12 期", "24 期", "36 期"]
            elif "申请人与抵押物权属人关系" == check:
                true_list = ["本人", "父母", "配偶", "子女"]
            elif "收款对象类型" == check:
                true_list = ["第三方机构", "合作单位"]
            for i in range(0, len(true_list)):
                self.check_Equal(true_list[i], lis[i].get_attribute("textContent"), check + "列表校验失败")

    def check_finance(self, finance_data): ##检验打款信息
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
        self.check_Equal(ture_sf_money, sf_money, "首付金额计算有误（首付金额=车辆价格-贷款金额合计）")
        self.check_Equal(true_sf_proportion, sf_proportion, "首付比例计算有误（首付比例=首付金额/车辆价格*100%）")
        self.check_Equal(ture_first_month_money, first_month_money, "首月还款计算有误（首月还款=（贷款金额合计+手续费总额）-月还款金额×（贷款期数-1））")
        self.check_Equal(true_month_money, month_money, "月还款金额计算有误(月还款金额=贷款金额合计/贷款期数+手续费总额/贷款期数)")
        self.check_Equal(true_poundage_amount, poundage_amount, "手续费总额计算有误(手续费总额=贷款金额合计×分期手续费率)")
        self.check_Equal(true_loan_money, loan_money, "贷款金额合计计算有误(贷款金额合计 = 实际贷款额 + 实际贷款额×（总利率 - 分期手续费率）)")
        self.check_Equal(ture_contract_sf_ratio, contract_sf_ratio, "收入还贷比计算有误(收入还贷比=其他月还款额/还款人月均总收入)")
        self.check_Equal(insureamt, car_price, "车损险投保金额和车辆价格不符")
        self.check_Equal(mortvalue, car_price, "抵押品价值和车辆价格不符")

    def check_Equal(self, first, second, msg=None):
        try:
            self.assertEqual(first, second, msg=None)
        except AssertionError:
            catch_image(self.browser)
            raise

    def checkIsNotNone(self,obj,msg=None):
        try:
            self.assertIsNotNone(obj,msg=None)
        except AssertionError:
            catch_image(self.browser)
            raise

    def Claim(self, car_type):  ##认领操作
        element = find_element(self.browser, By.LINK_TEXT, "开卡分期/承保申请")
        element_click(element)
        element_click(find_element(self.browser, By.ID, "tab-1"))
        self.claim_input_car_type(car_type)
        find_element(self.browser, By.CLASS_NAME, "has-gutter")  # 隐性等待，等待列表元素都展示出来
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "button", "认领"))

    def UnClaim(self):  ##退件操作
        element = find_element(self.browser, By.LINK_TEXT, "开卡分期/承保申请")
        element_click(element)
        element_click(find_element(self.browser, By.ID, "tab-2"))
        find_element(self.browser, By.CLASS_NAME, "has-gutter")  # 隐性等待，等待列表元素都展示出来
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "button", "退件"))

    def Handle(self, car_type):  ##处理操作
        element = find_element(self.browser, By.LINK_TEXT, "开卡分期/承保申请")
        element_click(element)
        element_click(find_element(self.browser, By.ID, "tab-2"))
        self.unclaim_input_car_type(car_type)
        find_element(self.browser, By.CLASS_NAME, "has-gutter")  # 隐性等待，等待列表元素都展示出来
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "button", "处理"))

    def claim_input_car_type(self, car_type): ##待认领搜索车型
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

    def unclaim_input_car_type(self, car_type):##待处理搜索车型
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

    def storage(self):#暂存操作
        element_click(find_element_by_text(self.browser, By.TAG_NAME, "button", "暂存"))

    def submit(self):#提交操作
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

    def test_CardSuccess(self):
        '''开卡分期/承保申请测试'''
        car_type = "新车"
        self.Claim(car_type)
        self.Handle(car_type)
        self.card()
        self.stage()
        # self.storage()
        self.submit()

    def tearDown(self):
        self.log.log_info("开卡_分期测试结束")
        time.sleep(10)
        self.driver.tearDown()
