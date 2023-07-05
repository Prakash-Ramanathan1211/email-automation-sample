import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, render_template, Response, request, redirect
import os.path

app = Flask(__name__)
# @app.route('/',methods=["GET"])
# def start():
#     return "hi"

@app.route('/send/mail/<email>/<filename>',methods=["GET"])
def index(email,filenam):

    body = '''Hello,
    This is the body of the email
    sicerely yours
    G.G.
    '''
    # put your email here
    sender = 'yuvibro1211@gmail.com'
    # get the password in the gmail (manage your google account, click on the avatar on the right)
    # then go to security (right) and app password (center)
    # insert the password and then choose mail and this computer and then generate
    # copy the password generated here
    password = 'tiecqtzjasbhectc'
    # put the email of the receiver here
    receiver = email

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'This email has an attacment, a pdf file'

    message.attach(MIMEText(body, 'plain'))

    filenam = filenam+".pdf"

    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__,filenam),'rb') as pdf:
        print(pdf)
        # pdfname = '/api/rank-test.pdf'

        # pdfname = open(pdf, 'rb')

        

        payload = MIMEBase('application', 'octate-stream', Name=filenam)
        # payload = MIMEBase('application', 'pdf', Name=pdfname)
        payload.set_payload((pdf).read())

        # enconding the binary into base64
        encoders.encode_base64(payload)
        
        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=filenam)
        message.attach(payload)

        #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)

        #enable security
        session.starttls()

        #login with mail_id and password
        session.login(sender, password)

        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()
        print('Mail Sent')

    return "true"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
