from ..app.app import db

class Customer( db.Model ):
	id = db.Column( db.Integer(), primary_key=True )
	customer_uri = db.Column( db.String( 512 ) )
	transactions = db.relationship( "Transaction", backref=db.backref( "customer" ) )

	def __init__( self, customer_uri ):
		self.customer_uri = customer_uri

		db.Model.__init__( self )

	@property
	def serialize( self ):
		return { "id": self.id,
			 "customer_uri": self.customer_uri,
			 "transactions": [ i.serialize for i in self.transactions ] }
