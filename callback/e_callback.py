#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/14 11:10
# software: PyCharm
from function import *

'''E分期回调，transType=
{1：征信回退，2：开卡分期回退，3：订单拒绝，4：征信通过，5:抵押补录，
6：材料补录，7：银行放款，8：抵押通知，9：订单取消}'''


def e_callback(transType, orderNo, businessType):
    url = get("url", "e_callback_url")
    api = "/api/efenqi/callback"
    url = url + api
    if transType in [1, 2, 3, 4, 5, 8, 9]:
        req = {"transType": transType, "opinion": None}
    elif transType in [6]:
        req = {"transType": transType, "opinion": "银行卡流水缺失", "materials": {"mateCover": [], "mateAdded": {
            "mates": [{"mateName": "银行卡流水", "mateCode": "yhls"}], "taskId": 701}}}
    elif transType in [7]:
        if businessType == "mobile":
            loanResult = [{"loanInfo": [
                {"trxspot": "山东林润汽车销售服务有限公司", "firstamt": 1700, "loanAccount": "16020000210126733", "loanFlag": 1,
                 "eachdate": 10, "workdate": "2019-11-10", "eachpfee": 151, "eachamt": 1680, "nextdate": "2019-12-10",
                 "firstpfee": 160, "loanAmount": 60500, "feeamt": 5445}], "loanStageDate": None, "recstatMsg": "放款成功",
                "loanDate": None, "recstat": "73", "cardNo": "6212268137029688516"}]
        elif businessType == "car":
            loanResult = [{"loanInfo": [], "loanStageDate": None, "loanDate": None, "recstat": "50"}]
        req = {"transType": transType, "loanResult": loanResult, "opinion": None}
    json_data = {"assurerNo": "S16024754", "bankType": "ICBC", "orgCode": "linrun", "busiCode": "1004",
                 "pub": {"bankCode": "0180400023", "assurerNo": "S16024754", "orderNo": orderNo,
                         "bankType": "ICBC", "platNo": "linrun"}, "platNo": "linrun",
                 "req": req}
    result = http_post(url, querystring=None, json=json_data, payload=None, headers=None)
    code = json.loads(result)["code"]
    time_code = json.loads(time_action())["code"]
    if code == time_code == 0:
        return True
    else:
        return False


def time_action():
    url = get("url", "time_url")
    platform = get("env", "platform")
    qs = "name=" + platform
    result = http_get(url, querystring=qs, headers=None)
    return result


if __name__ == '__main__':
    time_action()
