#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 12:58
# software: PyCharm
import unittest
class check():
    def checkEqual(self, first, second, msg):
        self.assertEqual(first,second,msg)



if __name__ == '__main__':

    a=check()
    a.checkEqual("1","2","不相等")


