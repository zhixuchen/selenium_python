#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/16 13:05
# software: PyCharm
from function import *


def get(title, string):
    try:
        root_path = os.path.abspath(os.path.dirname(__file__)).split('selenium_python')[0]
        path = root_path + "\\selenium_python\\function\\config"
        config = configparser.ConfigParser()
        config.read(path + "\\Config.ini")
        result = config.get(title, string)
        return result
    except Exception as e:
        logging.error("获取配置报错：" + e)


if __name__ == '__main__':
    print(get("url", "web_url"))
    print(get("account", "xs_account"))
