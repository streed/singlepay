from flask import request
from flask.ext import restful

from flask.ext.security.decorators import roles_required

from ..security.secure_access import secure

class Merchants( restful.Resource ):

	@secure
	@roles_required( "merchant" )
	def get( self ):
		return { "merchants": [] }

	@secure
	@roles_required( "merchant" )
	def post( self ):
		data = request.form["data"]

		return { "merchants": [] }

class Merchant( restful.Resource ):

	@secure
	@roles_required( "merchant" )
	def get( self, merchant_id ):
		return { "merchant": {} }

	@secure
	@roles_required( "merchant" )
	def put( self, merchant_id ):
		data = request.form["data"] 

		return { "merchant": {} }
