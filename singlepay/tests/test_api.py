import unittest

from ..app.app import app
from ..client.client import SinglePay, SinglePayPermissionsError
from nose.tools import assert_equals, assert_raises

class TestApi( unittest.TestCase ):

	def setUp( self ):
		app.config["TESTING"] = True
		self.app = app.test_client()

		client = SinglePay( public="sean@singlepay.me", private="password" )
		client.get = self.app.get
		client.post = self.app.post
		client._url = ""

		self.client = client

	def test_api_with_correct_credentials( self ):
		response = self.client.customers()
		assert len( response ) > 0

	def test_api_with_incorrect_credentials( self ):
		self.client.private = "password1"
		assert_raises( SinglePayPermissionsError, self.client.customers )

	def test_api_find_customer( self ):
		customer = self.client.customer.create().set_id( 1 ).find()

		assert_equals( "/test/uri/1", customer.customer_uri )

	def test_api_find_merchant( self ):
		merchant = self.client.merchant.create().set_id( 1 ).find()

		assert_equals( "/test/uri/4", merchant.merchant_uri )

	def test_api_create_transaction( self ):
		customer = self.client.customer.create().set_id( 1 ).find()
		merchant = self.client.merchant.create().set_id( 1 ).find()

		transaction = self.client.transaction.create().set_amount( 100 ).set_timestamp( 10000000 ).set_message( "This is a test" ).set_customer( customer ).set_merchant( merchant ).save()

		print transaction
