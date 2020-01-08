#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2018/10/16 11:30
# software: PyCharm
from driver.google_driver import *
import time
from database.db_conect import *

LOG_NAME = time.strftime("%Y-%m-%d", time.localtime(time.time())) + '.log'
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename=LOG_NAME, level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)


def mysql(sql):
    ip = get("config", "ip")
    account = get("config", "account")
    pwd = get("config", "pwd")
    da_name = get("config", "da_name")
    RESULT = mysqlconect(ip, account, pwd, da_name, sql)
    if len(RESULT) > 0:
        result = RESULT[0][0]
    else:
        result = True
    return result


def job():
    browser = web_diiver()
    url="https://car.xiaojukeji.com/order/"
    browser.get(url)
    browser.delete_all_cookies()
    browser.implicitly_wait(5)

    # 设置cookie
    # cookie=getCookie()
    # for key in cookie:
    # 	print({"name":key, "value":cookie[key]})
    # 	driver.add_cookie({"name":key, "value":cookie[key]})

    browser.add_cookie({"name": "NewSSO_SESSIONID",
                       "value": "Z0dZci8ySGNlZEVya2R4YzIxZUhoTys1bWpDZGFDMmxwWTMvYk9YMDg2UzFIR29OT3c1L1ozS2FoMDBPak5ZNQ%3D%3D"})
    browser.add_cookie({"name": "NewAutoCompanyUser",
                       "value": "bDA5bkhxUk9MR29tTmg4SGFVcFZwREdOYVRzOVBWNTZZTnlaY0VrT3oySzhaN0prVGk0cHM2blF1NEhnZG5rWFhRSUE3UTl1T2Z6dVo0N2VKQ2tHVU9SaGl2c3hwTy9BTm5qM3hKb0JtZVhGb1pBL1JOQlRSZ3g1MGNoOWd0dERKNnM3ZTNqbWR6bUJrWXl3U3ZqM2UyazhENnhqOFpqRHREcEhkZUpMQVpvNWJjdy9RRjN1cnZGRTVHNjl5bGJZ"})
    browser.add_cookie({"name": "AutoCompanyUser",
                       "value": "bDA5bkhxUk9MR29tTmg4SGFVcFZwREdOYVRzOVBWNTZZTnlaY0VrT3oySzhaN0prVGk0cHM2blF1NEhnZG5rWFhRSUE3UTl1T2Z6dVo0N2VKQ2tHVU9SaGl2c3hwTy9BTm5qM3hKb0JtZVhGb1pBL1JOQlRSZ3g1MGNoOWd0dERKNnM3ZTNqbWR6bUJrWXl3U3ZqM2UyazhENnhqOFpqRHREcEhkZUpMQVpvNWJjdy9RRjN1cnZGRTVHNjl5bGJZ"})

    # 刷新页面
    browser.refresh()


    browser.find_element_by_xpath("//li[@data-menuid='3006']").click()

    # 点击“履约中”

    try:
        browser.find_element(By.CSS_SELECTOR,"[class='ant-spin ant-spin-spinning']")
    except Exception as e:
        print("213")
        time.sleep(2)
        element=find_element_click(browser,By.ID,"react-tabs-2")
        element.click()
    # stri=driver.find_element_by_id("react-tabs-2")
    # element = find_element_click(browser, By.ID, "react-tabs-2")
    # print(element)
    # element.click(

    "//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div[1]/div"

    time.sleep(10)



if __name__ == '__main__':
    try:
        job()




    except Exception as e:
        logging.error("报错信息：" + e)
