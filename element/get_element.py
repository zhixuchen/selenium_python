#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/10 10:40
# software: PyCharm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  time


def find_element(browser,by,String):
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((by, String)))
    element=browser.find_element(by, String)
    return element


def find_elements(browser,by,String):
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((by, String)))
    element=browser.find_elements(by, String)
    return element