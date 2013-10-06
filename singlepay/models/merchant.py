from ..app.app import db

class Merchant( db.Model ):
	id = db.Column( db.Integer(), primary_key=True )
	merchant_uri = db.Column( db.String( 512 ) )
	transactions = db.relationship( "Transaction", backref=db.backref( "merchant" ) )

	def __init__( self, merchant_uri ):
		self.merchant_uri = merchant_uri

		db.Model.__init__( self )

	@property
	def serialize( self ):
		return { "id": self.id,
			 "merchant_uri": self.merchant_uri,
			 "transactions": [ i.serialize for i in self.transactions ] }
