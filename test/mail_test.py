import pytest

from mail.mail import Mail

def test_send_email():
    email = Mail()
    first_name = "Saymon"
    last_name= "T"
    client_email = "saymon@email.com"
    reply_to = f"{first_name} {last_name} <{client_email}>"

    email.send_email(reply_to, "Teste Serverless", "Enviando E-mail do python serverless")

    assert True == True