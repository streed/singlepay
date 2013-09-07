from ..app.app import db

class Transaction( db.Model ):
	id = db.Column( db.Integer(), primary_key=True )
	amount = db.Column( db.Integer() )
	timestamp = db.Column( db.DateTime() )
	message = db.Column( db.String( 128 ) )

	merchant_id = db.Column( db.Integer(), db.ForeignKey( "merchant.id" ) )
	customer_id = db.Column( db.Integer(), db.ForeignKey( "customer.id" ) )

	@property
	def serialize( self ):
		return { "id": self.id,
			 "amount": self.amount,
			 "timestamp": self.timestamp,
			 "message": self.message,
			 "customer": self.customer,
			 "merchant": self.merchant }
