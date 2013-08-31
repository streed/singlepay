import uuid
from singlepay.app import app
from singlepay.db import db, db_session

class Ledger( db.Model ):
	id = db.Column( db.Integer() primary_key=True )
	
	transactions = db.relationship( "Transaction", backref="ledger" )

