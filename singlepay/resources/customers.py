from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse

from flask.ext.security import login_required

from ..security.secure_access import secure

parser = reqparse.RequestParser()


class Customers( restful.Resource ):

	@secure
	def get( self ):
		return {"customers": [] }

	@secure
	def post( self ):
		data = request.form["data"]

		return { "customers": [] }

class Customer( restful.Resource ):

	def get( self, customer_id ):
		return { "customer": {} }

	def put( self, customer_id ):
		data = request.form["data"]

		return { "customer": {} }
