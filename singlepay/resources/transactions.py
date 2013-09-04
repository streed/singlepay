
from flask import request
from flask.ext import restful

from flask.ext.security.decorators import roles_accepted

from ..security.secure_access import secure

class Transactions( restful.Resource ):

	@secure
	@roles_accepted( "customer", "merchant" )
	def get( self, _type="" ):
		print _type
		ret = {}
		ret[_type] = [ { "id": 1, "amount": 100, "timestamp": 10000, "message": "test" } ]

		return ret

	@secure
	@roles_accepted( "customer", "merchant" )
	def post( self, _type ):
		data = request.form["data"]

		ret = {}
		ret[_type] = {}

		return ret

class Transaction( restful.Resource ):

	@secure
	@roles_accepted( "customer", "merchant" )
	def get( self, _type, transaction_id ):
		return { "transaction": {} }

	@secure
	@roles_accepted( "customer", "merchant" )
	def put( self, _type, transaction_id ):
		data = request.form["data"]

		return { "transaction": {} }
