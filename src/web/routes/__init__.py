from typing import NamedTuple
from web.controllers import TmpController, TmpDatabaseController
from web.pages import TmpPage
from .interface import SimpleRoute, RegexpRoute
from .tmp_simple_routes import TmpOne, TmpTwo, TmpThree
from .tmp_regexp_routes import TmpMatch
from .tmp_database_routes import ContactRootRoute, ContactIdRoute


class SimpleRoutesDependencies(NamedTuple):
    tmp_controller: TmpController
    tmp_page: TmpPage
    tmp_database_controller: TmpDatabaseController

def get_simple_routes(dependencies: SimpleRoutesDependencies) -> dict[str, SimpleRoute]:
    simple_routes: dict[str, SimpleRoute] = {}
    simple_routes_array: list[SimpleRoute] = [
        TmpOne(dependencies.tmp_controller),
        TmpTwo(dependencies.tmp_page),
        TmpThree(dependencies.tmp_page),
        ContactRootRoute(dependencies.tmp_database_controller)
    ]

    for route in simple_routes_array:
        simple_routes[route.path] = route
    return simple_routes

class RegexpRoutesDependencies(NamedTuple):
    tmp_database_controller: TmpDatabaseController

# pylint: disable=unused-argument
def get_regexp_routes(dependencies: RegexpRoutesDependencies) -> list[RegexpRoute]:
    return [
        TmpMatch(),
        ContactIdRoute(dependencies.tmp_database_controller)
    ]
