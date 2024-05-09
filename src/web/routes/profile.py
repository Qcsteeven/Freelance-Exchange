from web.controllers import ResponseJSON
from web.server import Web
from dtos import Validator, CustomerProfile
from .interface import SimpleRoute

class ChangeCoustomerProfileInfo(SimpleRoute):
    path = '/customer/profile'
    methods = ['POST']

    def handle(self, req: Web, method: str) -> dict:
        try:
            customer_profile: CustomerProfile = Validator.parse(req.get_body(), CustomerProfile)
            print(customer_profile.id, customer_profile.name, customer_profile.email)
            # code ...
        except:
            return ResponseJSON({'message': False})
        return ResponseJSON({'message': True})