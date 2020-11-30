import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from .env import HOST_UMBLER, PORT_UMBLER, USER_UMBLER, PASS_UMBLER

class Mail(object):
    host = HOST_UMBLER
    port = PORT_UMBLER
    user = USER_UMBLER
    password = PASS_UMBLER

    def __init__(self):
        pass

    def send_email(self, reply_to, subject, message):
        # set up the SMTP server
        s = smtplib.SMTP(host=self.host, port=self.port)
        s.starttls()
        s.login(self.user, self.password)

        msg = MIMEMultipart()  # create a message

        # setup the parameters of the message
        msg['From'] = self.user
        msg['To'] = self.user
        msg['Reply-To'] = reply_to
        msg['Subject'] = subject

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)

        del msg