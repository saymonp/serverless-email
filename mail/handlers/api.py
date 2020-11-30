import json
from ..util import lambda_method
from ..errors import AppError
from mail.mail import Mail


@lambda_method
def send_email(event, context):
    try:
        body = json.loads(event['body'])

        first_name = body["firstName"]
        last_name = body["lastName"]
        client_email = body["clientEmail"]
        subject = body["subject"]
        message = body["message"]
        
        reply_to = f"{first_name} {last_name} <{client_email}>"

        email = Mail()
        email.send_email(reply_to, subject, message)


        return {"ok": "Email sent"}
    except Exception as e:
        raise AppError(f"Email sending failed {e}")