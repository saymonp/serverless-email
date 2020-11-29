from ..util import lambda_method
from ..errors import AppError


@lambda_method
def send_email(event, context):
    try:
        first_name = event["firstName"]
        last_name = event["lastName"]
        client_email = event["clientEmail"]
        subject = event["subject"]
        message = event["message"]

        return {"first_name": first_name, "last_name": last_name, "client_email": client_email, "subject": subject, "message": message}
    except:
        raise AppError("Email sending failed")
