class CodeNotFound(Exception):
    message = 'CODE_NOT_FOUND'

class CodeIncorrectly(Exception):
    message = 'CODE_INCORRECTLY'

class RegSessionNotFound(Exception):
    message = 'REG_SESSION_NOT_FOUND'

class EmailException(Exception):
    message = 'EMAIL_EXCEPTION'

class EmailNowUsed(Exception):
    message = 'EMAIL_NOW_USED'

class LoginException(Exception):
    message = 'LOGIN_EXCEPTION'

class SessionNotFound(Exception):
    message = 'SESSION_NOT_FOUND'

class SessionExpired(Exception):
    message = 'SESSION_EXPIRED'
