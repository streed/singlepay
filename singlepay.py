from flask import Flask

from singlepay.processors.processors import processors
from singlepay.customers.customers import customers
from singlepay.information.information import information

app = Flask( __name__ )

app.register_blueprint( processors, url_prefix="/processors" )
app.register_blueprint( customers, url_prefix="/customers" )
app.register_blueprint( information, url_prefix="/information" )

if __name__ == "__main__":
	app.run()
