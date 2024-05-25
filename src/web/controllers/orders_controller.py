from storage import Storage


class OrdersController:
    storage: Storage

    def __init__(self, storage: Storage):
        self.storage = storage
