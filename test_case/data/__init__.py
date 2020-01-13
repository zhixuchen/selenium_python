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
        self.account=get("account", "xs_account")
        self.pwd=get("pwd", "xs_pwd")
        self.sms_code='123456'
        self.user1info=User()
        self.user2info = User()
        self.user3info = User()
        self.user4info = User()

class Test_Data():
    def __init__(self):
        self.credit_image_titles=['身份证人像面','身份证国徽面','征信授权书','手持征信授权书']
        self.credit_input_titles=['姓名','身份证号','手机号','业务类型','贷款银行','意向价格','银行卡号','家庭住址','签发机关','身份证有效期','长期有效']

if __name__ == '__main__':
    try:
        a=Data()
        print(a.user1info.name)
        print(a.user2info.name)
    except Exception as e:
        print("")


