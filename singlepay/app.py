from flask import Flask
from flask.ext.restful import Api
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, login_required

from resources.customers import Customers, Customer
from resources.merchants import Merchants, Merchant
from resources.transactions import Transactions, Transaction

app = Flask( __name__ )

app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "yay"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

api = Api( app )

api.add_resource( Customers, "/customers" )
api.add_resource( Customer, "/customer/<int:customer_id>" )

api.add_resource( Merchants, "/merchants" )
api.add_resource( Merchant, "/merchant/<int:merchant_id>" )

api.add_resource( Transactions, "/trasactions/<string:_type>" )
api.add_resource( Transaction, "/transaction/<string:_type>/<int:transaction_id>" )

db = SQLAlchemy( app )

from models.api_user import ApiUser, ApiRole
api_datastore = SQLAlchemyUserDatastore( db, ApiUser, ApiRole )

security = Security( app, api_datastore )

from security.secure_access import secure_unauthorized
app.login_manager.unauthorized = secure_unauthorized

@app.before_first_request
def create_user():
	db.create_all()
	api_datastore.create_user( email="sean@cheapfit.me", password="password" )
	db.session.commit()

