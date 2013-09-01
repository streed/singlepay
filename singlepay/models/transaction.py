from singlepay.db import db

class Transaction( db.Model ):
	id = db.Column( db.Integer(), primary_key=True )
	amount = db.Column( db.Integer() )
	timestamp = db.Column( db.DateTime() )
	message = db.Column( db.String( 128 ) )

	merchant_id = db.Column( db.Integer(), db.ForeignKey( "merchant.id" ) )
	customer_id = db.Column( db.Integer(), db.ForeignKey( "customer.id" ) )

