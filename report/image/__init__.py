#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 18:31
# software: PyCharm


from  function.driver import *
import os
import time
# 生成年月日时分秒时间
def catch_image(driver):
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    # 打印文件目录
    root_path = os.path.abspath(os.path.dirname(__file__)).split('selenium_python')[0]
    # 获取到当前文件的目录，并检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
    try:
        File_Path = root_path+'\\selenium_python\\report\\image\\' + directory_time + '\\'
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
    except BaseException as msg:
        print("新建目录失败：%s" % msg)

    try:
        driver.save_screenshot(root_path+'\\selenium_python\\report\\image\\' + directory_time + '\\' + picture_time + '.png')
    except BaseException as pic_msg:
        print("截图失败：%s" % pic_msg)

