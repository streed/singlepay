from builder import Builder

from ..models import Customer as CustomerModel

class Customer( Builder ):
	_attributes_ = { "id": None, "customer_uri": None, "transactions": [] }
	_model_ = CustomerModel

