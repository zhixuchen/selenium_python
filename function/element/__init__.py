#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/16 10:50
# software: PyCharm


import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_elemntsbyelemnt(element,by,string):
    webelements=element.find_elements(by,string)
    return webelements

def find_elemntbyelemnt(element,by,string):
    webelement=element.find_element(by,string)
    return webelement

def element_send_key(element, key):
    element.clear()
    element.send_keys(key)

def element_click(element):
    time.sleep(0.5)
    while (not element.is_enabled()):
        print("不可点击")
        if (element.is_enabled()):
            element.click()
            print("发现元素，并已经点击")
            break
    element.click()




def find_elementbytext(browser, by, string,text):
    elements=find_elements(browser, by, string)
    for element in elements:
        if text==element.text:
            return element



def find_element(browser, by, string):
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((by, string)))
    element = browser.find_element(by, string)
    return element


def find_elements(browser, by, string):
    time.sleep(0.5)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((by, string)))
    element = browser.find_elements(by, string)
    return element


def find_element_send_key(browser, by, string, key):
    find_element(browser, by, string).clear()
    find_element(browser, by, string).send_keys(key)

def find_element_click(browser,by,String):
    time.sleep(1)
    element = find_element(browser,by,String)
    while (not element.is_enabled()):
        print("不可点击")
        if (element.is_enabled()):
            element.click()
            print("发现元素，并已经点击")
            break
    element.click()