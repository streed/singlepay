from flask import request
from flask.ext import restful

class Merchants( restful.Resource ):
	def get( self ):
		return { "merchants": [] }

	def post( self ):
		data = request.form["data"]

		return { "merchants": [] }

class Merchant( restful.Resource ):
	def get( self, merchant_id ):
		return { "merchant": {} }

	def put( self, merchant_id ):
		data = request.form["data"] 

		return { "merchant": {} }
