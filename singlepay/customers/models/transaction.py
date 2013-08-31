import uuid

from singlepay.app import app
from singlepay.db import db, db_session

class Transaction( db.Model ):
	id = db.Column( db.Integer(), primary_key=True )
	amount = db.Column( db.Integer() )
	date = db.Column( db.DateTime() )
	message = db.Column( db.String( 144 ) )
	ledger_id = db.Column( db.Integer(), db.ForeignKey( "ledger.id" ) )
	debitor_id = db.Column( db.Integer(), db.ForeignKey( "customer.id" ) )
	creditor_id = db.Column( db.Integer(), db.ForeignKey( "customer.id" ) )

	debitor = db.relationship( "Customer", backref="debits" )
	creditor = db.relationship( "Cutsomer", backref="credits" )
