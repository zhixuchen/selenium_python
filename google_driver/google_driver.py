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


def web_diiver():
    path = os.path.dirname(os.path.realpath(sys.executable))  # 项目执行路径
    driver_path = path + "\\selenium_driver\\chromedriver.exe"
    web_browser = webdriver.Chrome(driver_path)
    web_browser.maximize_window()
    return web_browser


if __name__ == '__main__':
    browser = web_diiver()
    url = "http://release.web.beta.lrwanche.com"
    browser.get(url)
    find_element(browser, By.NAME, "username").clear()
    find_element(browser, By.NAME, "username").send_keys("15000000001")
    find_element(browser, By.NAME, "password").clear()
    find_element(browser, By.NAME, "password").send_keys(123456)
    find_element(browser, By.TAG_NAME, "button").click()
