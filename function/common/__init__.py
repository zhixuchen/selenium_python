#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 12:58
# software: PyCharm


def test():
    try:
        s = None
        if s is None:
            print(len(s))

          # 这句不会执行，但是后面的except还是会走到
    except Exception as e:
        print(e)

    test1()
def test1():
    print("234234234")

if __name__ == '__main__':

    test()


