from singlepay.client.client import SinglePay

if __name__ == "__main__":
	s = SinglePay()

	"""c = s.customers()

	print c
	for i in c:
		print i.transactions

	print s.debits()
	print s.credits()

	m = s.merchants()
	"""
	print s.customer.create().set_customer_uri( "/hello" ).set_id( 9999 ).finalize().id
