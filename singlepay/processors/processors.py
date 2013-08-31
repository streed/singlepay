from flask import Blueprint, render_template, abort

processors = Blueprint( "processors", __name__ )

@processors.route( "/" )
def index():
	return "Hello, processors."
