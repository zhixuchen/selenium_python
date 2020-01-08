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

if __name__ == '__main__':
    try:
        a=Data()
        print(a.user1info.name)
        print(a.user2info.name)
    except Exception as e:
        print("")


