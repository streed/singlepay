from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse

from flask.ext.security import login_required
from flask.ext.security.decorators import roles_required

from ..security.secure_access import secure

parser = reqparse.RequestParser()


class Customers( restful.Resource ):

	@secure
	@roles_required( "customer" )
	def get( self ):
		return {"customers": [ { "id": 1, "customer_uri": "http://fake.com", "transactions": [ { "id": 2, "amount": 200, "message": "yay this works", "timestamp": 1000000 } ] }] }

	@secure
	@roles_required( "customer" )
	def post( self ):
		data = request.form["data"]

		return { "customers": [] }

class Customer( restful.Resource ):

	@secure
	@roles_required( "customer" )
	def get( self, customer_id ):
		return { "customer": {} }

	@secure
	@roles_required( "customer" )
	def put( self, customer_id ):
		data = request.form["data"]

		return { "customer": {} }
