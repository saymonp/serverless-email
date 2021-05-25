import pytest

from mail.mail import Mail


def test_send_email():
    email = Mail()
    to = "contato@saymontrevisan.space"
    subject = "Email de Verificação"
    message = "Enviando E-mail do python serverless"
    first_name = "Saymon"
    last_name = "T"
    client_email = "saymon@email.com"
    reply_to = f"{first_name} {last_name} <{client_email}>"

    email.send_email(to, reply_to, subject, message)

    assert True == True
