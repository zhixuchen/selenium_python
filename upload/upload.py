#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/10 10:40
# software: PyCharm
from element.get_element import *
import os,sys

global path
path=os.path.dirname(os.path.realpath(sys.executable))#打包后的项目路径
path=os.path.split(os.path.abspath(__file__))[0]#调试根目录
def upload_image(browser,By,String,file_dir,file_list):
    global path
    for file_name in file_list:
        time.sleep(0.2)
        find_element(browser,By,String).click()  # 点击上传
        up_load_path = path+"\\upimage.exe"
        file_path=file_dir + file_name
        os.system('%s  %s' % (up_load_path, file_path))#调用AutoIt进行上传操作
        time.sleep(0.2)

if __name__ == '__main__':
   print()