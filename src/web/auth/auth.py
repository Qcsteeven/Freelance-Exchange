from os import urandom
from string import ascii_letters, digits
from secrets import choice
from asyncio import sleep, create_task
from hashlib import sha512
from .exceptions import CodeNotFound, CodeIncorrectly, RegSessionNotFound, EmailNowUsed, LoginException
from .email import Email


class Session:
    def get(self):
        pass

    def delete(self):
        pass

    def add(self):
        pass

class AuthSystem:
    email: Email
    messages_with_code: list[list[str, str]] = []
    signup_sessions: dict[str, str] = {}

    def __init__(self, email: Email):
        self.email = email

    def login(self, email: str, password: str):
        # TODO: check user
        db_password = ''# TODO: getting code
        salt = db_password.split(':')[0]
        password_hashed = self._hashing(password, salt)

        if password_hashed != db_password:
            raise LoginException()

        # TODO: generate session key and saving

    def get_user(self, session: str):
        # TODO: database request
        pass

    def logout(self, session: str):
        # TODO: check database
        # TODO: delete session in database
        pass

    def send_code(self, email: str):
        self._check_email(email)
        message = [email, self.email.send_code(email)]
        self.messages_with_code.append(message)
        create_task(self._delete_code_message_with_delay(message))

    def check_code(self, email: str, code: int) -> str:
        self._check_code(email, code)
        session_key = ''
        unique = False

        while unique:
            session_key = self._generate_session_key()

            if not self.signup_sessions[session_key]:
                self.signup_sessions[session_key] = email
                unique = True
                create_task(self._delete_reg_session_with_delay(session_key))

        return session_key

    def check_reg_session(self, session: str) -> bool:
        return self.signup_sessions.get(session) is not None

    def signup(self, session: str, first_name: str, second_name: str, password: str, customer: bool) -> str:
        if not self.check_reg_session(session):
            raise RegSessionNotFound()

        # TODO: check email in database
        password_hashed = self._hashing(password)
        # TODO: create new user

    def _check_email(self, email: str):
        for msg in self.messages_with_code:
            if msg[0] == email:
                raise EmailNowUsed()

        for session in self.signup_sessions:
            if self.signup_sessions.get(session) == email:
                raise EmailNowUsed()

    def _generate_session_key(self) -> str:
        alphabet = ascii_letters + digits + '_'
        session_key = ''.join(choice(alphabet) for _ in range(64))
        return session_key

    def _hashing(self, password: str, salt: bytes = None) -> str:
        if salt is None:
            salt = urandom(32)

        sha = sha512()
        sha.update(salt)
        sha.update(password.encode())
        hashed_password = sha.hexdigest()
        return f"{salt.hex()}:{hashed_password}"

    async def _delete_reg_session_with_delay(self, session: str):
        sleep(60 * 60)
        if self.signup_sessions.get(session) is not None:
            del self.signup_sessions[session]

    async def _delete_code_message_with_delay(self, message: list[str, int]):
        sleep(60)
        try:
            self.messages_with_code.remove(message)
        except ValueError:
            pass

    def _check_code(self, email: str, code: int):
        for message in self.messages_with_code:
            message_email = message[0]
            message_code = message[1]

            if message_email == email:
                if message_code != code:
                    self.messages_with_code.remove(message)
                    raise CodeIncorrectly()
                self.messages_with_code.remove(message)
                return
        raise CodeNotFound()
