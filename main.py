from project.config import Config
from project.storage import Storage
from project.web.server import start_server
from project.web.routes import get_simple_routes, get_regexp_routes
from project.web.controllers.tmp_controller import TmpController
# from project.web.controllers.orders_controller import OrdersController
# from project.web.controllers.customer_controller import CustomerController
# from project.web.controllers.performer_controller import PerformerController


def get_controllers_for_simple_routes(storage: Storage) -> dict:
    return {
        'tmp_controller': TmpController(storage),
        # 'order_controller': OrdersController(storage),
        # 'customer_controller': CustomerController(storage),
        # 'performer_controller': PerformerController(storage),
    }

def get_controllers_for_regexp_routes(storage: Storage) -> dict:
    return {
        # 'tmp_controller': TmpController(storage),
        # 'order_controller': OrdersController(storage),
        # 'customer_controller': CustomerController(storage),
        # 'performer_controller': PerformerController(storage),
    }

def main():
    config = Config()
    storage = Storage(config.get_database_url())

    simple_routes_controllers = get_controllers_for_simple_routes(storage)
    regexp_routes_controllers = get_controllers_for_regexp_routes(storage)

    simple_routes = get_simple_routes(**simple_routes_controllers)
    regexp_routes = get_regexp_routes(**regexp_routes_controllers)

    start_server(simple_routes, regexp_routes, config.get_server_port())


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('long KeyboardInterrupt exception message.')
