#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/10 10:40
# software: PyCharm
from element.get_element import *
import os
import sys

global project_path
# path = os.path.dirname(os.path.realpath(sys.executable))# 打包后的项目路径
project_path = os.path.split(os.path.abspath(__file__))[0]# 调试根目录


def upload_image(browser, by, string, file_dir, file_list):
    global project_path
    for file_name in file_list:
        time.sleep(0.2)
        find_element(browser, by, string).click()  # 点击上传
        up_load_path = project_path+"\\upimage.exe"
        file_path = file_dir + file_name
        os.system('%s  %s' % (up_load_path, file_path))  # 调用AutoIt进行上传操作
        time.sleep(0.2)

