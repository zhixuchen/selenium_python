#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 17:56
# software: PyCharm
from function.customize import *
from function.config import *
class Data():
    def __init__(self):
        self.url=get("url", "web_url")
        self.sms_code='123456'

    def get_account(self,account):
        self.result=get("account",account)
        return self.result

    def get_pwd(self,pwd):
        self.result=get("pwd",pwd)
        return self.result

    def get_userinfo(self):
        self.userinfo = User()

        return self.userinfo


class Test_Data():
    def __init__(self):
        self.credit_image_titles=['身份证人像面','身份证国徽面','征信授权书','手持征信授权书']
        self.credit_input_titles=['姓名','身份证号','手机号','业务类型','贷款银行','意向价格','银行卡号','家庭住址','签发机关','身份证有效期','长期有效']

if __name__ == '__main__':
    try:
        a=Data()
        print(a.get_userinfo().name)
        print(a.get_userinfo().name)
        print(a.get_account("kk_account"))
        print(a.get_pwd("kk_pwd"))
        print(a.get_account("cs_account"))
        print(a.get_pwd("cs_pwd"))
        # print(a.getuserinfo().user.name)
    except Exception as e:
        print("")


