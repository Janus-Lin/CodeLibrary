"""
CodeLibrary.smtplib_eg
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2022-01-06
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


me = '15403330314@qq.com'
you = '15403330314@qq.com'

try:
    s = smtplib.SMTP()
    s.connect('smtp.263.net')
    s.login(me, 'me s password')

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Alert 主题"
    msg['From'] = me
    msg['To'] = you

    html = '<html><body><p>Hi, I have the following alerts for you!</p></body></html>'
    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    s.sendmail(me, you, msg.as_string())
    s.quit()

except Exception as  e:
    print(e)

