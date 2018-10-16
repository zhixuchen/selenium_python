#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/10 10:40
# software: PyCharm
import os
if __name__ == '__main__':
    print(os.system('%s' % ("pyinstaller -F  main_test.py")) ) # 调用s_AutoIt进行上传操作