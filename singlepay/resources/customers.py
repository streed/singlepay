from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse

from flask.ext.security import login_required
from flask.ext.security.decorators import roles_required

from ..security.secure_access import secure

from ..models.customer import Customer as CustomerModel

parser = reqparse.RequestParser()


class Customers( restful.Resource ):

	@secure
	@roles_required( "customer" )
	def get( self ):
		return { "customers": [ i.serialize for i in CustomerModel.query.all() ] }

	@secure
	@roles_required( "customer" )
	def post( self ):
		data = request.form["data"]

		return { "customers": [ i.serialize for i in CustomerModel.query.all() ] }

class Customer( restful.Resource ):

	@secure
	@roles_required( "customer" )
	def get( self, customer_id ):
		return { "customer": CustomerModel.query.filter_by( id=customer_id ).first().serialize }

	@secure
	@roles_required( "customer" )
	def put( self, customer_id ):
		data = request.form["data"]

		return { "customer": CustomerModel.query.filter_by( id=customer_id ).first().serialize }
