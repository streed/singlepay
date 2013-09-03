from singlepay.client.client import SinglePay

if __name__ == "__main__":
	s = SinglePay()

	print s.customers()
	print s.debits()
	print s.credits()
