#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 13:00
# software: PyCharm

from selenium import webdriver
import os
import sys

class Driver():
    def __init__(self):
        self.path=os.path.dirname(os.path.realpath(sys.executable))  # 项目执行路径
        self.driver_path= self.path + "\\selenium_driver\\chromedriver.exe"
        self.chrome_browser=webdriver.Chrome(self.driver_path)
        self.chrome_browser.maximize_window()
    def tearDown(self):
        self.chrome_browser.quit()



if __name__ == '__main__':
    browser = Driver()
    url = "http://zxchen-web-docker-zxchen.beta.saasyc.com"
    browser.chrome_browser.get(url)
    browser.tearDown()
