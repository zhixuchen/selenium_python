#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 12:51
# software: PyCharm
import os

if __name__ == '__main__':
    try:
        cmd = 'taskkill /F /IM chromedriver.exe'
        os.system(cmd)
    except Exception as e:
        print(e)
