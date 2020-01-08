#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 17:12
# software: PyCharm
import unittest


class Test_Case (unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        self.assertEqual (6, 6)

    def test_add2(self):

        self.assertEqual (6, 11)

    def tearDown(self):
        print("test end")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test_Case('test_add2'))
    suite.addTest (Test_Case ('test_add'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
