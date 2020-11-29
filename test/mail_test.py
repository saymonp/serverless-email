import pytest

from mail.mail import Mail

def test_send_email():
    email = Mail()
    email.send_email("saymon@email.com", "Teste enviando E-mail do python serverless")
    assert True == True