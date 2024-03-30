from http import HTTPStatus
from typing import Callable
from .controllers.tmp_controller import TmpController
from .controllers.interfaces import Response, ResponseType
from .pages.tmp import TmpPage
from .server import Web


simple_routes: dict[str, Callable[[Web], Response]] = {
    "/tmp-1" : lambda req : TmpController().tmp_method(),
    "/tmp-2" : lambda req : Response(
        type=ResponseType.HTML,
        body=TmpPage().generate(req.path),
        status_code=HTTPStatus.OK
    )
}
