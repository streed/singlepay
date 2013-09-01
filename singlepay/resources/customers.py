from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse

parser = reqparse.RequestParser()


class Customers( restful.Resource ):
	def get( self ):
		return {"customers": [] }

	def post( self ):
		data = request.form["data"]

		return { "customers": [] }

class Customer( restful.Resource ):

	def get( self, customer_id ):
		return { "customer": {} }

	def put( self, customer_id ):
		data = request.form["data"]

		return { "customer": {} }
