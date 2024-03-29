from controllers.user_controller import UserController
from pages.auth import AuthPage
from types import Response

patches = {
    "/login" : lambda req : UserController().login(req),
    "/auth" : lambda req : Response(type='html', body=AuthPage().generate()),
}