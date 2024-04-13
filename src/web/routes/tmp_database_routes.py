from re import Match, compile as regexp_compile
from web.exceptions import BadRequest, NotFound
from web.controllers import TmpDatabaseController, ResponseJSON
from web.server import Web
from .interface import RegexpRoute



class ContactRootRoute(RegexpRoute):
    regexp = regexp_compile(r'^/db/(?P<table>\w+)/?$')
    methods = ['GET', 'POST']
    _db_controller: TmpDatabaseController

    def __init__(self, db_controller: TmpDatabaseController):
        self._db_controller = db_controller

    def handle(self, req: Web, match: Match, method: str) -> ResponseJSON:
        table = match.group('table')

        if method == 'GET':
            return self._db_controller.select_all(table)
        elif method == 'POST':
            body = req.get_body()
            if body is None:
                raise BadRequest()
            return self._db_controller.insert(table, body)
        else:
            raise NotFound()

class ContactIdRoute(RegexpRoute):
    regexp = regexp_compile(r'^/db/(?P<table>\w+)/(?P<contact_id>\d+)/?$')
    methods = ['GET', 'POST', 'DELETE']
    _db_controller: TmpDatabaseController

    def __init__(self, db_controller: TmpDatabaseController):
        self._db_controller = db_controller

    def handle(self, req: Web, match: Match, method: str) -> ResponseJSON:
        table = match.group('table')
        contact_id = match.group('contact_id')

        if method == 'GET':
            return self._db_controller.select_one(table, contact_id)
        elif method == 'POST':
            body = req.get_body()
            if body is None:
                raise BadRequest()
            return self._db_controller.update(table, contact_id, body)
        elif method == 'DELETE':
            return self._db_controller.delete(table, contact_id)
        else:
            raise NotFound()
