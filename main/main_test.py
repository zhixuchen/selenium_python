#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/16 11:30
# software: PyCharm
from google_driver.google_driver import *
import time
from config.get_config_ini import *
LOG_NAME = time.strftime("%Y-%m-%d", time.localtime(time.time()))+'.log'
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename=LOG_NAME, level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


if __name__ == '__main__':
    try:
        browser = web_diiver()
        url = get("config", "url")
        browser.get(url)
        find_element(browser, By.NAME, "username").clear()
        find_element(browser, By.NAME, "username").send_keys(get("account", "xs"))
        find_element(browser, By.NAME, "password").clear()
        find_element(browser, By.NAME, "password").send_keys(get("pwd", "xs"))
        find_element(browser, By.TAG_NAME, "button").click()
    except Exception as e:
        logging.error("报错信息："+e)

