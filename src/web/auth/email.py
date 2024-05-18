from smtplib import SMTP
from secrets import choice
from email.mime.text import MIMEText
from .exceptions import EmailException


class Email:
    server: SMTP
    email: str

    def __init__(self, email: str, password: str):
        self.email = email
        self.server = SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(email, password)

    def send_code(self, email: str) -> str:
        code = self._generate_code()

        try:
            self.server.sendmail(self.email, email, self._get_message(code))
        except Exception as e:
            raise EmailException() from e

        return code

    def _generate_code(self) -> str:
        return ''.join(choice('0123456789') for _ in range(6))

    def _get_message(self, code: str) -> str:
        message = MIMEText(f'Код для авторизации: {code}')
        message['Subject'] = 'Код для авторизации'
        return message.as_string()
