#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2020/1/8 12:52
# software: PyCharm
import smtplib
import time
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from BeautifulReport import BeautifulReport  # 导入BeautifulReport

from function.config import *

root_path = os.path.abspath(os.path.dirname(__file__)).split('selenium_python')[0]
path = root_path + "\\selenium_python\\report\\html\\"

send_email = get("email", "send_email")
send_pwd = get("email", "send_pwd")
to_email = get("email", "to_email")
to_name = get("email", "to_name")
from_name = get("email", "from_name")
my_sender = send_email  # 发件人邮箱账号
my_pass = send_pwd  # 发件人邮箱密码
my_user = to_email  # 收件人邮箱账号，我这边发送给自己
my_user = my_user.split(',')
directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))

class Report():
    def build_report(suite_tests, report_name, description):
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

        report_name = report_name + picture_time
        try:
            File_Path = path + directory_time + '\\'
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
        except BaseException as msg:
            print("新建目录失败：%s" % msg)
        try:
            BeautifulReport(suite_tests).report(filename=report_name, description=description,
                                                report_dir=File_Path)
            return File_Path + report_name + '.html'

        except BaseException as pic_msg:
            print("生成报告失败：%s" % pic_msg)

    def sent_email(name):
        ret = True
        try:
            message = MIMEMultipart()
            message['From'] = Header(from_name, 'utf-8')
            message['To'] = Header(to_name, 'utf-8')
            message['Subject'] = Header('自动化测试报告', 'utf-8')
            filename=name.split(directory_time+"\\")[1]
            html = Report.addAttach(name, filename=filename)  # 自动化测试报告附件
            message.attach(html)
            server = smtplib.SMTP_SSL("smtp.mxhichina.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, my_user, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
            print("邮件发送成功")
        except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            print(e)
            ret = False
            print("邮件发送失败")
        return ret

    def addAttach(apath, filename='Report.html'):
        with open(apath, 'rb') as fp:
            attach = MIMEBase('application', 'octet-stream')
            attach.set_payload(fp.read())
            attach.add_header('Content-Disposition', 'attachment', filename=filename)
            encoders.encode_base64(attach)
            fp.close()
            return attach

    def report(suite_tests,report_name,description):
        try:
            name = Report.build_report(suite_tests, report_name, description)
            Report.sent_email(name)
        except Exception as e:
            return False
        return True


if __name__ == '__main__':
    Report.sent_email("C:\\Users\\Administrator\\Desktop\\new_file.html")
