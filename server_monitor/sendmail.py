#!/usr/bin/python
# coding: utf-8
# 这个脚本用于在25端口封堵的阿里云服务器上面发送邮件，利用qq邮箱的465端口发送
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTP_SSL
import string

mail_host = 'smtp.qq.com'
mail_user = '1078060960'
mail_passwd = 'gqfuozfboadjbacf'

sender = '1078060960@qq.com'
receivers = ['caochuanxing@aspirecn.com', '18939954234@139.com']
subject = '阿里云系统巡检报告'

f = open('/home/xingge/server_monitor/result.txt', 'rb')
text = "".join(f.readlines())

message = MIMEMultipart()
message.attach(MIMEText(text, 'plain', 'utf-8'))  # 添加正文内容
message['From'] = sender
message['To'] = ",".join(receivers)
message['Subject'] = Header(subject, 'utf-8')

# 添加附件
att1 = MIMEText(open('/home/xingge/server_monitor/server_monitor.py', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="result"'
message.attach(att1)

f.close()

if __name__ == '__main__':
    try:
        smtp = SMTP_SSL(mail_host, 465)
       # smtp.set_debuglevel(1)
        smtp.ehlo(mail_host)
        smtp.login(mail_user, mail_passwd)
        smtp.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"

    except Exception, e:
        print "失败,%s" % e

