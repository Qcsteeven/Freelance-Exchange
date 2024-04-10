from re import Match, compile as regexp_compile
from web.exceptions import BadRequest, NotFound
from web.controllers import TmpDatabaseController, ResponseJSON
from web.server import Web
from .interface import SimpleRoute, RegexpRoute



class ContactRootRoute(SimpleRoute):
    path = '/db/contacts'
    methods = ['GET', 'POST']
    _db_controller: TmpDatabaseController

    def __init__(self, db_controller: TmpDatabaseController):
        self._db_controller = db_controller

    def handle(self, req: Web, method: str) -> ResponseJSON:
        if method == 'GET':
            return self._db_controller.contacts_select_all()
        elif method == 'POST':
            body = req.get_body()
            if body is None:
                raise BadRequest()
            return self._db_controller.contacts_insert(body['email'], body['telephone'])
        else:
            raise NotFound()

class ContactIdRoute(RegexpRoute):
    regexp = regexp_compile(r'^/db/contacts/(?P<contact_id>\d+)/?$')
    methods = ['GET', 'POST', 'DELETE']
    _db_controller: TmpDatabaseController

    def __init__(self, db_controller: TmpDatabaseController):
        self._db_controller = db_controller

    def handle(self, req: Web, match: Match, method: str) -> ResponseJSON:
        contact_id = match.group('contact_id')

        if method == 'GET':
            return self._db_controller.contacts_select_one(contact_id)
        elif method == 'POST':
            body = req.get_body()
            if body is None:
                raise BadRequest()
            return self._db_controller.contacts_update(contact_id, body['email'], body['telephone'])
        elif method == 'DELETE':
            return self._db_controller.contacts_delete(contact_id)
        else:
            raise NotFound()
