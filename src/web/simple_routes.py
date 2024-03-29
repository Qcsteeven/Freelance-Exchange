from typing import Callable
from controllers.tmp_controller import TmpController
from controllers.interfaces import Response
from pages.tmp import TmpPage
from .web import Web


simple_routes: dict[str, Callable[[Web], Response]] = {
    "/tmp-1" : lambda req : TmpController().tmp_method(),
    "/tmp-2" : lambda req : Response(type='html', body=TmpPage().generate(req.path), status_code=200),
}
