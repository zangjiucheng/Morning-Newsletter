# -*- coding: utf-8 -*-

# Not working yet

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from settings import send_mail_adress, SMTP_server, port, login_password, receiver_mail_adress_list
from time import sleep
import sys

def send_post(data,status, email_adress):
    try:
        if len(email_adress) == 0:
            for receiver_mail_adress in receiver_mail_adress_list:
                mail(data.mail_data , send_mail_adress, SMTP_server,
                    port, login_password, receiver_mail_adress)
        else:
            mail(data.mail_data, send_mail_adress, SMTP_server,
                port, login_password, email_adress)

    except:
        print("Error")
        sys.exit(-1)
    if status == False:
        sleep(3600)


def mail(mail_data, send_mail_adress, SMTP_server, port, login_password, receiver_mail_adress):
    message = MIMEMultipart()
    message['From'] = send_mail_adress
    message['To'] = send_mail_adress
    message['Subject'] = "早报😀"
    image = MIMEImage(img_data, name=os.path.basename(x))
    image.add_header('Content-Id', 'image')
    inner.attach(image)
    message.attach(MIMEText(mail_data, 'plain'))
    message.attach(inner)
    session = smtplib.SMTP(SMTP_server, port)
    session.starttls()
    session.login(send_mail_adress, login_password)
    text = message.as_string()
    session.sendmail(send_mail_adress, receiver_mail_adress, text)
    session.quit()
    print('Mail Sent to:' + receiver_mail_adress)