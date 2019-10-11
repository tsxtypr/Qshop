from __future__ import absolute_import
from Qshop.celery import app
import requests

# 创建任务
@app.task   #将普通的函数转换为celery任务
def test():
    print('----i am test task----')
    return "i am test"

@app.task
def myprint(name,age):
    print("%s:%s"%(name,age))
    return 'i am myprint'

@app.task
def message():
    # url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"
    url = "http://106.ihuyi.com"

    # 短信平台信息
    account='C10415932'
    password='4acb3bf9a2d612d9d31f11f5843395c8'

    # 收件人手机号
    moblies="15137151071"
    # 短信内容
    content = "您的验证码是：1314。请不要把验证码泄露给其他人。"
    # 请求头
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/plain",
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'

    }

    # 构建发送参数
    data={
        'account':account,
        'password':password,
        "moblies":moblies,
        'content':content,
    }

    # 发送短信
    response=requests.post(url,headers=headers,data=data)

    print(response.content.decode())
    return '发送成功'
