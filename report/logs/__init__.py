#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 12:52
# software: PyCharm
import logging,os,time
from logging import handlers

root_path = os.path.abspath(os.path.dirname(__file__)).split('selenium_python')[0]
log_path=root_path+"selenium_python\\report\\logs\\"
log_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
class Logs():
    def __init__(self):
        try:
            File_Path = root_path + '\\selenium_python\\report\\logs\\' + directory_time + '\\'
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
        except BaseException as msg:
            print("新建目录失败：%s" % msg)
        self.log= Logger(File_Path+log_time+'.log',level='debug')
    def log_info(self,logs):
        self.log.logger.info(logs)
    def log_debug(self,logs):
        self.log.logger.debug(logs)
    def log_error(self,logs):
        self.log.logger.error(logs)
    def log_warning(self, logs):
        self.log.logger.warning(logs)
    def log_critical(self, logs):
        self.log.logger.critical(logs)


class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        # sh = logging.StreamHandler()#往屏幕上输出
        # sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        # self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)
if __name__ == '__main__':
    log=Logs()
    log.log_info("test")


