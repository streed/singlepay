from flask import Blueprint, render_template, abort

information = Blueprint( "information", __name__ )

@information.route( "/" )
def index():
	return "Hello, information." 
