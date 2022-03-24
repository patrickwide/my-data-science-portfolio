import smtplib

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

from ssl import create_default_context
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


email = "patkia911@gmail.com"

fromaddr = 'patkia911@gmail.com'
toaddr = email

msg = MIMEMultipart()

msg['From'] = fromaddr

msg['To'] = toaddr

msg['Subject'] = "patrick's resume"

body = "Hey my name is patrick,Thank you for requesting my resume"

msg.attach(MIMEText(body))

files = ['test_img.jpg', 'test_img.jpg']

for filename in files:
    my_file = os.path.join(THIS_FOLDER, filename)

    attachment = open(my_file, 'rb')

    part = MIMEBase("application", "octet-stream")

    part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header("Content-Disposition",f"attachment; filename= {filename}")

    msg.attach(part)

msg = msg.as_string()
print('hello world 1')

server = smtplib.SMTP_SSL('smtp.gmail.com',465, context=create_default_context())
print('hello world 2')

# server.ehlo()

# server.starttls()
# print('hello world 3')

# server.starttls(context=create_default_context())

server.login(fromaddr, 'gvfblpjgsqkrmjao')
print('hello world 4')

server.sendmail(fromaddr, toaddr, msg)
print('hello world 5')

server.quit()
print('hello world 6')














# import smtplib
# from email.mime.text import MIMEText
#
# from email.message import EmailMessage
# #from email import encoders
#
# email_user = 'my.email@email.com'
# email_send = input('Enter address to Send e-mail to: ')
# subject = 'Python!'
#
# msg = EmailMessage()
# msg['From'] = email_user
# msg['To'] = email_send
# msg['Subject'] = subject
#
# body = 'Hi there, This is a test E-mail from Python!' #This part is missing
# msg.attach(MIMEText(body, 'plain'))
#
#
# filename = 'my_file'
#
#
# with open(filename, 'rb') as content_file:
#     content = content_file.read()
#     msg.add_attachment(content, maintype='application/pdf', subtype='pdf', filename=filename)
#
# text = msg.as_string()
#
#
#
#
#
#
# server = smtplib.SMTP('server',port)
# server.sendmail(email_user, email_send, text)
# server.quit