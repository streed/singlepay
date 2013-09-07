import time
import os
import ConfigParser
from collections import namedtuple
from requests import get, post
from ..security.secure_access import _calc_signature
from .models import Transaction, Customer, Merchant

class SinglePay( object ):

	def __init__( self, public="", private="" ):
		self._url = "http://localhost:5000"

		if public == "" and private == "":
			config = ConfigParser.ConfigParser()
			config.readfp( open( os.path.expanduser( "~/.singlepay" ) ) )

			self.public = config.get("Keys", "public" )
			self.private = config.get( "Keys", "private" )

	def _make_request( self, method, action, body ):
		timestamp = int( time.time() )

		signature = _calc_signature( self.private, self.public, action, body, timestamp )

		headers = { "Timestamp": timestamp, "Signature": signature, "PublicKey": self.public }

		return method( "%s%s" % ( self._url, action ), data=body, headers=headers )

	def _transactions( self, _type ):
		response = self._make_request( get, "/transactions/%s" % _type, {} )

		response = response.json()

		return [ Transaction( self, **k ) for k in response[_type] ]

	def debits( self ):
		return self._transactions( "debits" )

	def credits( self ):
		return self._transactions( "credits" )

	def customers( self ):
		response = self._make_request( get, "/customers", {} )
		response = response.json()

		result = [ Customer( self, **k ) for k in response["customers"] ]

		return result

	def merchants( self ):
		response = self._make_request( get, "/merchants", {} )
		response = response.json()

		print response

		result = [ Merchant( self, **k ) for k in response["merchants"] ]

		return result
