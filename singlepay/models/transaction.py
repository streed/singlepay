from ..app.app import db

class Transaction( db.Model ):
	id = db.Column( db.Integer(), primary_key=True )
	amount = db.Column( db.Integer() )
	timestamp = db.Column( db.DateTime() )
	message = db.Column( db.String( 128 ) )

	merchant_id = db.Column( db.Integer(), db.ForeignKey( "merchant.id" ) )
	customer_id = db.Column( db.Integer(), db.ForeignKey( "customer.id" ) )

	merchant = db.relationship( "Merchant", backref=db.backref( "transactions", lazy="dynamic" ) )
	customer = db.relationship( "Customer", backref=db.backref( "transactions", lazy="dynamic" ) )

	def __init__( self, amount, timestamp, message, merchant, customer ):
		self.amount = amount
		self.timestamp = timestamp
		self.message = message
		self.merchant_id = merchant
		self.customer_id = customer

	def save( self ):
		db.session.add( self )
		db.session.commit()

	@property
	def serialize( self ):
		return { "id": self.id,
			 "amount": self.amount,
			 "timestamp": self.timestamp.isoformat(),
			 "message": self.message,
			 "customer": self.customer.id,
			 "merchant": self.merchant.id }

