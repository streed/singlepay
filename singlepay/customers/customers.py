from flask import Blueprint, render_template, abort

customers = Blueprint( "customers", __name__ )

@customers.route( "/" )
def index():
	return "Hello, customers."
