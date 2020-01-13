#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/10 10:40
# software: PyCharm
from function.element import *
import os
import sys
import time





def upload_images(browser, by, string, file_dir, file_list):
    project_path = os.path.dirname(os.path.realpath(sys.executable))  # 项目执行路径
    for file_name in file_list:
        time.sleep(0.2)
        find_element(browser, by, string).click()  # 点击上传
        up_load_path = project_path+"\\selenium_driver\\upimage.exe"
        file_path = file_dir + file_name
        os.system('%s  %s' % (up_load_path, file_path))  # 调用AutoIt进行上传操作
        time.sleep(0.2)


if __name__ == '__main__':
    root_path = os.path.abspath(os.path.dirname(__file__)).split('selenium_python')[0]
    up_load_path=root_path+"selenium_python\\function\\driver\\upimage.exe"
    print(up_load_path)