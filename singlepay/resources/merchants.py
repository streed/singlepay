from flask import request
from flask.ext import restful

from flask.ext.security.decorators import roles_required, roles_accepted

from secureresource import SecureResource

from ..models.merchant import Merchant as MerchantModel

class Merchants( SecureResource ):

	@roles_required( "internal", "merchant" )
	def get( self ):
		return { "merchants": [] }

	@roles_required( "internal", "merchant" )
	def post( self ):
		data = request.form["data"]

		return { "merchants": [] }

class Merchant( SecureResource ):

	@roles_required( "internal", "merchant" )
	def get( self, merchant_id ):
		return { "merchant": MerchantModel.query.filter_by( id=merchant_id ).first().serialize }

	@roles_required( "internal", "merchant" )
	def put( self, merchant_id ):
		data = request.form["data"] 

		return { "merchant": {} }
