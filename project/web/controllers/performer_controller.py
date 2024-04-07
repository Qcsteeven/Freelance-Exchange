from project.storage import Storage


class PerformerController:
    storage: Storage

    def __init__(self, storage: Storage):
        self.storage = storage
