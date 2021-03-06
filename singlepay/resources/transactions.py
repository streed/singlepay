
from flask import request
from flask.ext import restful

from flask.ext.security.decorators import roles_accepted, roles_required
import datetime

from secureresource import SecureResource
from ..models.transaction import Transaction as TransactionModel

class Transactions( SecureResource ):

	@roles_required( "internal" )
	@roles_accepted( "customer", "merchant" )
	def get( self, _type="" ):
		ret = {}
		ret[_type] = [ { "id": 1, "amount": 100, "timestamp": 10000, "message": "test" } ]

		return ret

	@roles_required( "internal" )
	@roles_accepted( "customer", "merchant" )
	def post( self ):
		data = request.form

		transaction = TransactionModel( int( data["amount"] ), 
					   datetime.datetime.strptime( data["timestamp"], "%Y-%m-%dT%H:%M:%S.%f" ),
					   data["message"], 
					   int( data["merchant"] ), 
					   int( data["customer"] ) )
		transaction.save()

		ret = { "transaction": transaction.serialize }

		return ret

class Transaction( SecureResource ):

	@roles_accepted( "customer", "merchant" )
	def get( self, owner_type, owner_id,  _type, transaction_id ):
		return { "transaction": {} }

	@roles_accepted( "customer", "merchant" )
	def put( self, owner_type, owner_id,  _type, transaction_id ):
		data = request.form["data"]

		return { "transaction": {} }
