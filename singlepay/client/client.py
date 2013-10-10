import time
import os
import ConfigParser
from collections import namedtuple
from requests import get, post
from ..security.secure_access import _calc_signature
from .models import Transaction, Customer, Merchant
from .builders.customer import Customer as CustomerBuilder
from .builders.merchant import Merchant as MerchantBuilder
from .builders.transaction import Transaction as TransactionBuilder
from .errors import SinglePayError, SinglePayPermissionsError, SinglePayInvalidMethodError

class SinglePay( object ):

	get = get
	post = post

	def __init__( self, public="", private="" ):
		self._url = "http://localhost:5000"

		if public == "" and private == "":
			config = ConfigParser.ConfigParser()
			config.readfp( open( os.path.expanduser( "~/.singlepay" ) ) )

			self.public = config.get("Keys", "public" )
			self.private = config.get( "Keys", "private" )
		else:
			self.public = public
			self.private = private

		self.__customer_builder = CustomerBuilder( self )
		self.__merchant_builder = MerchantBuilder( self )
		self.__transaction_builder = TransactionBuilder( self )

	def _make_request( self, method, action, body ):
		if method == "get":
			method = self.get
		elif method == "post":
			method = self.post
		else:
			raise SinglePayInvalidMethodError( method )

		timestamp = int( time.time() )
		signature = _calc_signature( self.private, self.public, action, body, timestamp )
		headers = { "Timestamp": timestamp, "Signature": signature, "PublicKey": self.public }

		response = method( "%s%s" % ( self._url, action ), data=body, headers=headers )

		print response.data, action

		try:
			response = response.json()
		except AttributeError:
			import json
			response = json.loads( response.data )

		return response

	def _transactions( self, _type ):
		response = self._make_request( get, "/transactions/%s" % _type, {} )

		return [ Transaction( self, **k ) for k in response[_type] ]

	def debits( self ):
		return self._transactions( "debits" )

	def credits( self ):
		return self._transactions( "credits" )

	def customers( self ):
		response = self._make_request( "get", "/customers", {} )

		if "customers" in response:

			result = [ Customer( self, **k ) for k in response["customers"] ]

			return result
		else:
			raise SinglePayPermissionsError( "/customers" )

	def merchants( self ):
		response = self._make_request( "get", "/merchants", {} )

		result = [ Merchant( self, **k ) for k in response["merchants"] ]

		return result

	@property
	def customer( self ):
		return self.__customer_builder

	@property
	def merchant( self ):
		return self.__merchant_builder

	@property
	def transaction( self ):
		return self.__transaction_builder

