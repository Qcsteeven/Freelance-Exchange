from storage import Storage
from .interfaces import ResponseHTML


class TmpController:
    storage: Storage

    def __init__(self, storage: Storage):
        self.storage = storage

    def tmp_method(self, body: str = 'TmpController().tmp_method()'):
        return ResponseHTML(body=body)
