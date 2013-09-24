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

	_model_ = CustomerModel

	def __init__( self ):
		Builder.__init__( self )

		self._debitor = None
		self._creditor = None
		self._to_merchant = False

	def debit( self, other ):
		if isinstance( other, MerchantModel ):
			self._to_merchant = True

		self._debitor = other
	
	def credit( self, other ):
		if isinstance( other, MerchantModel ):
			self._to_merchant = False

		self._creditor = other	
