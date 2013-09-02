from ..app import db

class Merchant( db.Model ):
	id = db.Column( db.Integer(), primary_key=True )

	merchant_uri = db.Column( db.String( 512 ) )

	transactions = db.relationship( "Transaction", backref=db.backref( "merchant" ) )

