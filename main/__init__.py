#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/16 11:30
# software: PyCharm
import os

if __name__ == '__main__':
    # print(os.system('%s' % ("pip freeze > requirements.txt")))

    print(os.system('%s' % ("pip install -r requirements.txt")))