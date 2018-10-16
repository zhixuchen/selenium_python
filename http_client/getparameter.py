#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/10 10:40
# software: PyCharm

import urllib3
import json

def http_get(url):
    # 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
    http = urllib3.PoolManager()
    # 通过request()方法创建一个请求：
    r = http.request('GET', url)
    dict=json.loads(r.data.decode())
    # 获得html源码,utf-8解码
    return dict

def http_post(url,datas):
    # 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
    http = urllib3.PoolManager()
    # 通过request()方法创建一个请求：
    r = http.request('POST', url, datas)
    dict=json.loads(r.data.decode())
    # 获得html源码,utf-8解码
    return dict

def get_getparameter(key):
    #对应的key：name（获取姓名）、tel（获取电话）、certificate（获取身份证号）、bank（银行卡号）
    url = 'http://getparameter.baozitest.top/?key='+key
    parameter = http_get(url).get(key)
    return parameter

if __name__ == '__main__':
    try:
        url="http://master.api.beta.lrwanche.com/Api/auth/applogin"
        datas={
                'account': 15000000002,
                'password': 'e10adc3949ba59abbe56e057f20f883e',
                'from': 'Android',
                'lginfo': "{'current_version':'2.0.11'}"
            }
        result= http_post(url,datas)
        print(result.get('result').get('token').get('token'))
    except Exception as e:
        print("")