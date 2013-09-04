
#Transaction = namedtuple( "Transaction", "id, amount, timestamp, message" )
#Customer = namedtuple( "Customer", "id, customer_uri, transactions" )
#Merchant = namedtuple( "Merchant", "id, merchant_uri, transactions" )

class Base( object ):
	
	def __init__( self, api=None ):
		self._api = api

	def __proxy_request( self, method, action, body ):
		return self._api._make_request( method, action, body )

class Transaction( Base ):

	def __init__( self, api, id=None, amount=None, timestamp=None, message=None ):
		Base.__init__( self, api )

		self._id = id
		self._amount = amount
		self._timestamp = timestamp
		self._message = message

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

	def refund( self ):
		return None

class Customer( Base ):

	def __init__( self, api, id=None, customer_uri=None, transactions=[] ):
		Base.__init__( self, api )

		self._id = id
		self._customer_uri = customer_uri
		self._transactions = [ Transaction( api, **i ) for i in transactions ]

		self._path = "/customer/%d" % self._id

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
		return None


class Merchant( Base ):
	def __init__( self, api, id=None, merchant_uri=None, transactions=[] ):
		Base.__init__( self, api )

		self._id = id
		self._merchant_uri = customer_uri
		self._transactions = [ Transaction( api, **i ) for i in transactions ]

		self._path = "/merchant/%d" % self._id

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

	def verify_bank( self ):
		return None

	def start_deposit( self ):
		return None
