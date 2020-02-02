#引入相应的包
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



# 发送地址，
# 输入SMTP服务器地址
# 此处根据不同服务商设置不同的值
smtpserver = 'smtp.163.com'
user = 'wutian3152@163.com'
password = 'gwl3152372'

#收件人信息
#
sender = user
receiver = '736498007@qq.com'
subject = '这是一个测试啊'




#MIMEtext三个重要参数
#1.邮件内容
#2. MIME子类型，在此案例中我们用plain表示text类型
#3. 邮件编码格式

msg = MIMEMultipart('mixed')
att = MIMEText("Hello ,I am G william","txt","utf-8")
##att  附件
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment; filename = "E:\\pythonworkplace\\StudyData\\Python高级语法\\net编程\\net编程.md"'


msg.attach(att)
msg['From'] = user
msg['To'] = receiver
msg['Subject'] = Header(subject, 'utf-8')




try:

    # 第一个是服务器地址，但一定是bytes格式，需要编码
    #第二个是服务器的接受访问接口
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    #登陆邮箱发送
    smtp.login(user,password)
    #发送邮件
    #三个参数
    #1. 发送地址
    #2. 接受地址，必须是list格式
    #3. 发送内容，作为字符串发送
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
except Exception as e:
    print(e)