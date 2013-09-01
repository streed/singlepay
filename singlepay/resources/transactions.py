
from flask import request
from flask.ext import restful

class Transactions( restful.Resource ):
	def get( self, _type ):
		return {}

	def post( self, _type ):
		data = request.form["data"]

		return {}

class Transaction( restful.Resource ):
	def get( self, _type, transaction_id ):
		return {}

	def put( self, _type, transaction_id ):
		data = request.form["data"]

		return {}
