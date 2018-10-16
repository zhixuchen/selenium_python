#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/10 10:40
# software: PyCharm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element(browser, by, string):
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((by, string)))
    element = browser.find_element(by, string)
    return element


def find_elements(browser, by, string):
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((by, string)))
    element = browser.find_elements(by, string)
    return element
