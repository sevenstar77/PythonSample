import mimetypes
import smtplib
import socket
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import traceback

# 받는 메일 서버(pop3)
# address : pop.gmail.com
# port = 995
# 보내는 메일 서버(smtp)
# address : smtp.gmail.com
# port = 465, 587

try:
    host = 'smtp.gmail.com'
    port = 587
    # img = 'logo.png'
    htmlImg = 'logo.html'

    senderMail = ''
    receiverMail = ''
    password = ''

    msg = MIMEBase('multipart', 'alternative')
    # MIMEBase('multipart', 'mixed')

    # text 보낼경우
    # text = 'test send'
    # msg = MIMEText(text)

    msg['Subject'] = 'gmail send test'
    msg['From'] = senderMail
    msg['To'] = receiverMail

    # mime text
    with open(htmlImg, 'rb') as images:
        imagePart = MIMEText(images.read(), 'html', _charset='utf-8')
        images.close()

    # mime img
    # imgFile = 'google.jpg'
    # imagedFile = open(imgFile, 'rb')
    # ImagePart = MIMEImage(imagedFile.read())
    # imagedFile.close()
    # msg.attach(imagePart)

    # MIMEBase 첨부
    msg.attach(imagePart)

    # email sending
    s = smtplib.SMTP(host, port)
    s.starttls()
    s.login(senderMail, password)
    s.sendmail(senderMail, [receiverMail], msg.as_string())
    s.close()

except:
    print(traceback.format_exc())