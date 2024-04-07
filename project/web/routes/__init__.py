from .interface import SimpleRoute, RegexpRoute
from .tmp_simple_routes import TmpOne, TmpTwo, TmpThree
from .tmp_regexp_routes import TmpMatch
from ..controllers.tmp_controller import TmpController


# Simple Route

def get_simple_routes(tmp_controller: TmpController) -> list[SimpleRoute]:
    simple_routes: dict[str, SimpleRoute] = {}
    simple_routes_array: list[SimpleRoute] = [
        TmpOne(tmp_controller),
        TmpTwo(),
        TmpThree()
    ]

    for route in simple_routes_array:
        simple_routes[route.path] = route
    return simple_routes


# Regexp Route
# regexp example
# re.compile(r'^/tmp-match/(?P<something_text>[^/]+)/?$').match('/tmp-match/hello').group('something_text')

def get_regexp_routes() -> list[RegexpRoute]:
    return [TmpMatch()]
