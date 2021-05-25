import json

from ..util import lambda_method
from ..errors import AppError
from mail.mail import Mail
from ..env import USER_UMBLER



@lambda_method
def send_email(event, context):
    body = json.loads(event["body"])

    first_name = body["firstName"]
    last_name = body["lastName"]
    client_email = body["clientEmail"]
    subject = body["subject"]
    message = body["message"]

    to = USER_UMBLER
    reply_to = f"{first_name} {last_name} <{client_email}>"

    email = Mail()
    response = email.send_email(to, reply_to, subject, message)

    return response
