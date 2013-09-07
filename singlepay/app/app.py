from flask import Flask
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required


app = Flask( __name__ )
db = SQLAlchemy( app )

app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "yay"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"

api = Api( app )

from ..resources.customers import Customers, Customer
from ..resources.merchants import Merchants, Merchant
from ..resources.transactions import Transactions, Transaction

api.add_resource( Customers, "/customers" )
api.add_resource( Customer, "/customer/<int:customer_id>" )

api.add_resource( Merchants, "/merchants" )
api.add_resource( Merchant, "/merchant/<int:merchant_id>" )

api.add_resource( Transactions, "/transactions/<_type>" )
api.add_resource( Transaction, "/transaction/<_type>/<int:transaction_id>" )

from ..models.api_user import ApiUser, ApiRole
from ..models.transaction import Transaction
from ..models.customer import Customer
from ..models.merchant import Merchant
api_datastore = SQLAlchemyUserDatastore( db, ApiUser, ApiRole )

security = Security( app, api_datastore )

from ..security.secure_access import secure_unauthorized
app.login_manager.unauthorized = secure_unauthorized

@app.before_first_request
def create_user():
	if app.config["DEBUG"]:
		db.drop_all()
		db.create_all()
		user = api_datastore.create_user( email="sean@cheapfit.me", password="password" )
		role = api_datastore.create_role( name="customer", description="Identitifies the user as a customer." )
		api_datastore.add_role_to_user( user, role )
		api_datastore.create_role( name="merchant", description="Identitifies a user as a merchant." )
		db.session.commit()

		create_customers()

def create_customers():
	cust = Customer( "/test/uri/1" )
	db.session.add( cust )
	cust = Customer( "/test/uri/2" )
	db.session.add( cust )
	cust = Customer( "/test/uri/3" )
	db.session.add( cust )

	merch = Merchant( "/test/uri/4" )
	db.session.add( merch )
	merch = Merchant( "/test/uri/5" )
	db.session.add( merch )
	merch = Merchant( "/test/uri/6" )
	db.session.add( merch )

	db.session.commit()
