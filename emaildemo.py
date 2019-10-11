# import smtplib
# from email.mime.text import MIMEText
#
#
# # 构建邮件
# # 主题
# subject="0715"
# # 发送内容
# content="123456"
# # 发件人
# sender="str_wjp@163.com"
# # 接收人
# rec="1798748115@qq.com"
# # 密码
# password='qaz123'
# # 构建邮件
# message=MIMEText(content,'plain','utf-8')
# message['subject']=subject
# message['Form']=sender
# message['To']=rec
#
# # 发送邮件
# smtp=smtplib.SMTP_SSL('smtp.163.com',465)
# smtp.login(sender,password)
# smtp.sendmail(sender,rec,message.as_string())
# smtp.close()

