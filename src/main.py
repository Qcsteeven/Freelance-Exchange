from config import Config
from storage import Storage
from web.routes import get_simple_routes, get_regexp_routes, SimpleRoutesDependencies, RegexpRoutesDependencies
from web.server import start_server
from web.controllers import TmpController, TmpDatabaseController
from web.pages import TmpPage
#, OrdersController, CustomerController, PerformerController


def get_controllers_for_simple_routes(storage: Storage) -> SimpleRoutesDependencies:
    return SimpleRoutesDependencies(
        tmp_controller=TmpController(storage),
        tmp_page=TmpPage(),
    )

def get_controllers_for_regexp_routes(storage: Storage) -> RegexpRoutesDependencies:
    return RegexpRoutesDependencies(
        tmp_database_controller=TmpDatabaseController(storage)
    )

def main():
    config = Config()
    storage = Storage(config.get_database_url())

    simple_routes_controllers = get_controllers_for_simple_routes(storage)
    regexp_routes_controllers = get_controllers_for_regexp_routes(storage)

    simple_routes = get_simple_routes(simple_routes_controllers)
    regexp_routes = get_regexp_routes(regexp_routes_controllers)

    start_server(simple_routes, regexp_routes, config.get_server_port())


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('long KeyboardInterrupt exception message.')
