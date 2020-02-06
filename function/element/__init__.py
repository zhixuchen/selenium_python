#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/16 10:50
# software: PyCharm

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

'''根据element查找elements'''


def find_elements_by_element(element, by, string):
    webelements = element.find_elements(by, string)
    return webelements


'''根据element查找element'''


def find_element_by_element(element, by, string):
    webelement = element.find_element(by, string)
    return webelement


'''根据element设置KEY'''


def element_send_key(element, key):
    element.clear()
    element.send_keys(key)


'''根据element触发点击'''


def element_click(element):
    time.sleep(0.5)
    while (not element.is_enabled()):
        print("不可点击")
        if (element.is_enabled()):
            element.click()
            print("发现元素，并已经点击")
            break
    element.click()


'''根据element用js进行点击'''


def element_click_script(browser, element):
    time.sleep(0.5)
    browser.execute_script("arguments[0].click()", element)


'''根据文本text查找element'''


def find_element_by_text(browser, by, string, text):
    elements = find_elements(browser, by, string)
    for element in elements:
        if text == element.text:
            return element



'''根据文本text查找element'''
'''通过element查找'''


def find_element_by_text_element(element, by, string, text):
    time.sleep(0.5)
    elements = find_elements_by_element(element, by, string)
    for element in elements:
        if text == element.text:
            return element



'''重写查找element,隐性等待10秒'''


def find_element(browser, by, string):
    element =WebDriverWait(browser, 10, 0.5).until(EC.visibility_of_element_located((by, string)))
    return element


'''重写查找elements,隐性等待10秒'''


def find_elements(browser, by, string):
    WebDriverWait(browser, 10, 0.5).until(EC.visibility_of_element_located((by, string)))
    element = browser.find_elements(by, string)
    return element

'''知道当前element，查找同级别的input'''
def find_next_input_by_element(element):
    select_element=find_next_element(element)
    select_input=find_element_by_element(select_element,By.TAG_NAME,"input")
    return select_input


'''知道当前element，查找同级别的inputs'''
def find_next_inputs_by_element(element):
    select_element=find_next_element(element)
    select_inputs=find_elements_by_element(select_element,By.TAG_NAME,"input")
    return select_inputs

'''知道当前element查找下一个同级的element'''
def find_next_element(element):
    next_element=find_element_by_element(element,By.XPATH,"./following::*")
    return next_element

'''知道前一个element，在后面第一个input中输入key'''
def next_input_send_key(element,key):
    element_send_key(find_next_input_by_element(element),key)

'''知道element，根据element内的label的标题，对相应的input输入key'''
def send_key_by_input_title(element,title,key):
    title_element=find_element_by_text_element(element,By.TAG_NAME,"label",title)
    next_input_send_key(title_element,key)




