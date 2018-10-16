#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/16 13:05
# software: PyCharm
import configparser
import logging


def get(title, string):
    try:
        config = configparser.ConfigParser()
        config.read("Config.ini")
        result = config.get(title, string)
        return result
    except Exception as e:
        logging.error("获取配置报错："+e)


if __name__ == '__main__':
    print(get("config", "url"))
