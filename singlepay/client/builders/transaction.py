from builder import Builder

from ..models import Transaction as TransactionModel
from ..models import Merchant as MerchantModel
from ..models import Customer as CustomerModel

class Transaction( Builder ):
	_attributes_ = { "id": -1, 
			 "amount": 0, 
			 "message": "Default Message", 
			 "timestamp": 0, 
			 "merchant": None, 
			 "customer": None }

	_model_ = TransactionModel

