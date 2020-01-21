#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 12:51
# software: PyCharm
import os,math

if __name__ == '__main__':
    try:
        cmd = 'taskkill /F /IM chromedriver.exe'
        os.system(cmd)

        finance_data={'car_price': '1680000', 'sf_money': '1448000', 'sf_proportion': '86.19', 'contract_sf_ratio': '141.00', 'first_month_money': '7080', 'month_money': '7056', 'poundage_amount': '22040', 'insureamt': '1680000', 'loan_money': '232000', 'mortvalue': '1680000', 'monthincome': '8000', 'monrepayamt': '4200', 'commission_fee_rate': '9.5', 'contract_loan_money': '200000', 'company_service_rate': '25.5', 'repay_period': '36 期'}
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
        true_sf_proportion = 100 * (sf_money / car_price)
        ture_sf_money = car_price - loan_money
        ture_contract_sf_ratio = (monrepayamt / monthincome)*100
        ture_first_month_money = (loan_money + poundage_amount) - month_money*(repay_period - 1)
        true_month_money = (loan_money + poundage_amount) / repay_period
        true_poundage_amount = loan_money * commission_fee_rate
        true_loan_money = contract_loan_money + contract_loan_money * (company_service_rate - commission_fee_rate)
        # print(round(true_sf_proportion,2))
        # print(round(ture_sf_money))
        # print(ture_contract_sf_ratio)
        # print(round(ture_first_month_money))
        # print(round(math.floor(true_month_money)))
        # print(round(true_poundage_amount))
        print(round(true_loan_money))
        print(contract_loan_money)
    except Exception as e:
        print(e)
