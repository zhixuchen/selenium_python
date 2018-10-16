#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/10 10:40
# software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from element.get_element import *
import os
import sys

global path
path = os.path.dirname(os.path.realpath(sys.executable))# 打包后的项目路径
path = os.path.split(os.path.abspath(__file__))[0]# 调试根目录
def web_diiver():
    global path
    driver_path = path + "\\chromedriver.exe"
    browser = webdriver.Chrome(driver_path)
    browser.maximize_window()
    return browser


if __name__ == '__main__':
    browser = web_diiver()
    url = "http://release.web.beta.lrwanche.com"
    browser.get(url)
    find_element(browser, By.NAME, "username").clear()
    find_element(browser, By.NAME, "username").send_keys("15000000001")
    find_element(browser, By.NAME, "password").clear()
    find_element(browser, By.NAME, "password").send_keys(123456)
    find_element(browser, By.TAG_NAME, "button").click()


