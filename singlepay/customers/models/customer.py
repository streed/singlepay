import uuiid
from singlepay.app import app
from singlepay.db import db, db_session

class Customer( db.Model ):
	id = db.Column( db.Integer(), primary_key=True )

	provider = db.relationship( "Provider", backref=db.backref( "customers" ), uselist=False )
	providerInfo = db.relationship( "ProviderInformation", backref=db.backref( "customer" ), uselist=False )
	ledger = db.relationship( "Ledger", backref="customer", uselist=False )


