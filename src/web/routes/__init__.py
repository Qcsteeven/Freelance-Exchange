from typing import NamedTuple
from web.controllers import TmpController
from web.pages import TmpPage
from .interface import SimpleRoute, RegexpRoute
from .tmp_simple_routes import TmpOne, TmpTwo, TmpThree
from .tmp_regexp_routes import TmpMatch


class SimpleRoutesDependencies(NamedTuple):
    tmp_controller: TmpController
    tmp_page: TmpPage

def get_simple_routes(dependencies: SimpleRoutesDependencies) -> dict[str, SimpleRoute]:
    simple_routes: dict[str, SimpleRoute] = {}
    simple_routes_array: list[SimpleRoute] = [
        TmpOne(dependencies.tmp_controller),
        TmpTwo(dependencies.tmp_page),
        TmpThree(dependencies.tmp_page)
    ]

    for route in simple_routes_array:
        simple_routes[route.path] = route
    return simple_routes

class RegexpRoutesDependencies(NamedTuple):
    pass

# pylint: disable=unused-argument
def get_regexp_routes(dependencies: RegexpRoutesDependencies) -> list[RegexpRoute]:
    return [TmpMatch()]
