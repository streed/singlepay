from builder import Builder

from ..models import Customer as CustomerModel

class Customer( Builder ):
	_attributes_ = { "id": -1 }
	_model_ = CustomerModel
