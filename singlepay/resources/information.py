from flask import request
from flask.ext import restful

from flask.ext.security.decorators import roles_required, roles_accepted

from secureresource import SecureResource

from ..models.transaction import Transaction

class Information( SecureResource ):

	def get( self ):
		return { "transactions": [ i.serialize for i in Transaction.query.all() ] }
