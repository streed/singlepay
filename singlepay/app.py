from flask import Flask
from flask.ext.restful import Api
from flask.ext.security import Security, SQLAlchemyUserDataStore

from resources.customers import Customers, Customer
from resources.merchants import Merchants, Merchant
from resources.transactions import Transactions, Transaction

from models.api_user import ApiUser, ApiRole

app = Flask( __name__ )

api = Api( app )

api.add_resource( Customers, "/customers" )
api.add_resource( Customer, "/customer/<int:customer_id>" )

api.add_resource( Merchants, "/merchants" )
api.add_resource( Merchant, "/merchant/<int:merchant_id>" )

api.add_resource( Transactions, "/trasactions/<string:_type>" )
api.add_resource( Transaction, "/transaction/<string:_type>/<int:transaction_id>" )

api_datastore = SQLAlchemyUserDataStore( db, ApiUser, ApiRole )
security = Security( app, api_datastore )
