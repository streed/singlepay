from builder import Builder

from ..models import Customer as CustomerModel

class Customer( Builder ):
	_attributes_ = { "id": -1, "customer_uri": "/", "transactions": [] }
	_model_ = CustomerModel
