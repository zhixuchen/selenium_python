#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 13:00
# software: PyCharm

from selenium import webdriver
import os
import time
root_path = os.path.abspath(os.path.dirname(__file__)).split('selenium_python')[0]
class Driver():
    def __init__(self):
        self.driver_path = root_path + "selenium_python\\function\\driver\\chromedriver.exe"
        self.chrome_browser=webdriver.Chrome(self.driver_path)
        self.chrome_browser.maximize_window()
    def tearDown(self):
        self.chrome_browser.quit()

def upload_image( file_dir, file_name):
    time.sleep(0.2)
    up_load_path=root_path+"selenium_python\\function\\driver\\upimage.exe"
    file_path = file_dir + file_name+'.png'
    os.system('%s  %s' % (up_load_path, file_path))  # 调用AutoIt进行上传操作

if __name__ == '__main__':
    browser = Driver()
    url = "http://zxchen-web-docker-zxchen.beta.saasyc.com"
    browser.chrome_browser.get(url)
    browser.tearDown()
