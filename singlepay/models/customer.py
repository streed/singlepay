from ..app import db

class Customer( db.Model ):
	id = db.Column( db.Integer(), primary_key=True )
	custmer_uri = db.Column( db.String( 512 ) )

	transactions = db.relationship( "Transaction", backref=db.backref( "customer" ) )

