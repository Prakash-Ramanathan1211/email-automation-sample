import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, request
import os.path
from urllib.parse import quote

app = Flask(__name__)

@app.route('/send/mail/<email>/<filena>/<username>', methods=["GET"])
def send_mail(email, filena, username):

    body = f'''Hello {username.upper()}

    You have successfully registered for KERNEL'23.
    Please make sure to reach the campus before 9 AM

    Note
    * Come in proper formal dress code(No entry if not followed).
    * College bus will be available from all parts of the city.
    * Producing ID card is mandatory
    * Breakfast and Lunch will be provided within the campus.

    To know about the events visit: https://kernel-2k23.vercel.app/kernel.html
    For any further clarification contact us at kernel23symposium@gmail.com

    Waiting to see you on occasion.

    Warm Regards
    KERNEL'23
    Registration Team Members
    '''

    sender = 'kernel23symposium@gmail.com'
    password = 'rweriuwugqodjdme'
    receiver = email

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = "Successfully registered"

    message.attach(MIMEText(body, 'plain'))
    filen = filena + ".pdf"
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, filen), 'rb') as pdf:
        payload = MIMEBase('application', 'octate-stream', Name=filen)
        payload.set_payload(pdf.read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=quote(filen))
        message.attach(payload)

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender, password)
        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()

    return "true"



@app.route("/send/mail/<email>/<name>/<phone>/<query>",methods=["GET"])
def send_contact(email,name,phone,query):
    return "hello"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
