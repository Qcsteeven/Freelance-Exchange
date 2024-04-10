from http import HTTPStatus

class ResponseException(Exception):
    code: int = HTTPStatus.INTERNAL_SERVER_ERROR
    message: str =  'Internal Server Error.'

class InternalServerError(ResponseException):
    pass

class NotFound(ResponseException):
    code = HTTPStatus.NOT_FOUND
    message = 'Not Found'

class BadRequest(ResponseException):
    code = HTTPStatus.BAD_REQUEST
    message = 'Bad Request'
