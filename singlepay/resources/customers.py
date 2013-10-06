from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse
from flask.ext.security.decorators import roles_required, roles_accepted

from secureresource import SecureResource

from ..models.customer import Customer as CustomerModel

class Customers( SecureResource ):

	@roles_accepted( "internal", "customer" )
	def get( self ):
		return { "customers": [ i.serialize for i in CustomerModel.query.all() ] }

	@roles_required( "internal", "customer" )
	def post( self ):
		data = request.form["data"]

		return { "customers": [ i.serialize for i in CustomerModel.query.all() ] }

class Customer( SecureResource ):

	@roles_accepted( "internal", "customer" )
	def get( self, customer_id ):
		return { "customer": CustomerModel.query.filter_by( id=customer_id ).first().serialize }

	@roles_required( "internal", "customer" )
	def put( self, customer_id ):
		data = request.form["data"]

		data = customer.validate( data )

		customer = CustomerModel( data["customer"]["customer_uri"] )

		customer.save()		

		return { "customer": CustomerModel.query.filter_by( id=customer_id ).first().serialize }
