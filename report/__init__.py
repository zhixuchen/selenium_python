#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 12:52
# software: PyCharm
import os
import time

from BeautifulReport import BeautifulReport  # 导入BeautifulReport

root_path = os.path.abspath(os.path.dirname(__file__)).split('selenium_python')[0]
path = root_path + "\\selenium_python\\report\\html\\"


def build_report(suite_tests,report_name,description):

    directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    # 打印文件目录
    # 获取到当前文件的目录，并检查是否有 directory_time 文件夹，如果不存在则自动新建 directory_time 文件
    try:
        File_Path = path + directory_time + '\\'
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
    except BaseException as msg:
        print("新建目录失败：%s" % msg)
    try:
        BeautifulReport(suite_tests).report(filename=report_name, description=description,
                                            report_dir=File_Path)
    except BaseException as pic_msg:
        print("生成报告失败：%s" % pic_msg)
