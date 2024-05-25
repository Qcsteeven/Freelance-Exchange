from storage import Storage


class CustomerController:
    storage: Storage

    def __init__(self, storage: Storage):
        self.storage = storage
