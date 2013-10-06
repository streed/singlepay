
#Transaction = namedtuple( "Transaction", "id, amount, timestamp, message" )
#Customer = namedtuple( "Customer", "id, customer_uri, transactions" )
#Merchant = namedtuple( "Merchant", "id, merchant_uri, transactions" )
from ..errors import SinglePayError

class Base( object ):
	
	def __init__( self, api=None ):
		self._api = api

	def _proxy_request( self, method, action, body ):
		return self._api._make_request( method, action, body )

	def __repr__( self ):
		klass = str( self.__class__ ).replace( "<class '", "" ).replace( "'>", "" )
		return "<%s id:%d>" % ( klass, self.id )

class Transaction( Base ):

	def __init__( self, api, id=None, amount=None, timestamp=None, message=None ):
		Base.__init__( self, api )

		self._id = id
		self._amount = amount
		self._timestamp = timestamp
		self._message = message

	def _finalize( self ):
		self._path = "/transaction/%d" % self._id

	@property
	def id( self ):
		return self._id

	@property
	def amount( self ):
		return self._amount

	@property
	def timetamp( self ):
		return self._timestamp

	@property
	def message( self ):
		return self._message

	def refund( self, owner ):
		return None

	@property
	def serialize( self ):
		return { "id": self.id,
			 "amount": self._amount,
			 "timestamp": self._timestamp,
			 "message": self._message }

class Customer( Base ):

	def __init__( self, api, id=None, customer_uri=None, transactions=[] ):
		Base.__init__( self, api )

		self._id = id
		self._customer_uri = customer_uri
		self._transactions = [ Transaction( api, **i ) for i in transactions ]

	def _finalize( self ):
		self._path = "/customer/%d" % self._id
		self._customer_uri = self._path

	def find( self ):
		self._finalize()
		result = self._proxy_request( "get", self._path, {} )

		if "customer" in result:
			return Customer( self._api, **result["customer"] )
		else:
			raise SinglePayError( "%s was not found." % self )

	@property
	def id( self ):
		return self._id

	@property
	def customer_uri( self ):
		return self._customer_uri

	@property
	def transactions( self ):
		return self._transactions

	def delete( self ):
		return None

	def debit( self, other ):
		return None

	def credit( self, other ):
		return None

	def refund( self, transaction ):
		return transaction.refund( self )

	@property
	def serialize( self ):
		return { "id": self.id,
			 "customer_uri": self.customer_uri,
			 "transactions": [ i.serialize for i in self.transactions ] }

class Merchant( Base ):
	def __init__( self, api, id=None, merchant_uri=None, transactions=[] ):
		Base.__init__( self, api )

		self._id = id
		self._merchant_uri = merchant_uri
		self._transactions = [ Transaction( api, **i ) for i in transactions ]

	def _finalize( self ):
		self._path = "/merchant/%d" % self._id

	def find( self ):
		self._finalize()
		result = self._proxy_request( "get", self._path, {} )

		if "merchant" in result:
			return Merchant( self._api, **result["merchant"] )
		else:
			raise SinglePayError( "%s was not found." % self )

	@property
	def id( self ):
		return self._id

	@property
	def merchant_uri( self ):
		return self._merchant_uri

	@property
	def transactions( self ):
		return self._transactions

	def delete( self ):
		return None

	def debit( self, other ):
		return None

	def credit( self, other ):
		return None

	def verify_bank( self ):
		return None

	def start_deposit( self ):
		return None

	@property
	def serialize( self ):
		return { "id": self.id,
			 "merchant_uri": self.merchant_uri,
			 "transactions": [ i.serialize for i in self.transactions ] }

