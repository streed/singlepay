from builder import Builder

from ..models import Merchant as MerchantModel

class Merchant( Builder ):
	_attributes_ = { "id": -1, "merchant_uri": "/", "transactions": [] }
	_model_ = MerchantModel

