from flask import Flask,render_template,request,redirect,session,jsonify,json
# Python code to illustrate Sending mail from
# your Gmail account
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders

import smtplib

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders



app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    feedback = "Welcome"
    return render_template("index.html",feedback=feedback)


@app.route('/send', methods=['POST','GET'])
def success():
    if request.method == "POST":
        name = str(request.form['name'])
        email = str(request.form['email'])

        if name == "" or email == "":
            feedback = "Error || Check Your Email"
            return render_template('index.html',feedback=feedback)

        else:
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
                attachment = open(filename, 'rb')

                part = MIMEBase("application", "octet-stream")

                part.set_payload(attachment.read())

                encoders.encode_base64(part)

                part.add_header("Content-Disposition",f"attachment; filename= {filename}")

                msg.attach(part)

            msg = msg.as_string()

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(fromaddr, 'police911.4089')
                server.sendmail(fromaddr, toaddr, msg)
                server.quit()
                feedback = "Success || Thank You"
                return render_template("success.html",feedback=feedback)
            except:

                feedback = "Error || Check Your Email"
                return render_template('index.html',feedback=feedback)

    else:
        return redirect('/')






if __name__ == "__main__":
    app.run(debug=True, port=7889)
