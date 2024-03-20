from customer import Customer
from request import Request
from company import Company

OrderOptions = {
  'title': str,
  'customer': Customer,
  'descriptions': str
}

class Order:
  descriptions: str

  def __init__(self):
    pass

  def create(self, options: OrderOptions):
    pass

  def close(self):
    pass

  def delete(self):
    pass

  def get_all_request(self) -> [Request]:
    pass

  def select_request(self, req: Request):
    pass

  def get_status(self):
    pass

  def get_customer(self):
    pass

  def get_compony(self) -> Company:
    pass

  def change_title(self):
    pass

  def change_description(self):
    pass
