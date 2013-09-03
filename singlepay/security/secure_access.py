import hashlib
import time
from functools import wraps
from flask import current_app, request, _request_ctx_stack
from flask.ext.security import login_required
from flask.ext.restful import reqparse
from werkzeug.local import LocalProxy

try:
	from urllib.parse import quote
except ImportError:
	from urllib import quote

#Grab a thread local proxy to the security extension.
_security = LocalProxy( lambda: current_app.extensions["security"] )


def _calc_signature( private, public, action, body ):
	signature = "%s|%s|%s|" % ( private, action, public )

	keys = sorted( body.keys() )

	body_strs = []
	for k in keys:
		body_strs.append( "%s=%s" % ( quote( k, safe='' ), quote( body[k], safe="-_~" ) ) )

	signature += "&".join( body_strs )

	sig = hashlib.sha512()
	sig.update( signature )

	return sig.hexdigest().strip().encode( "utf-8" )

def _check_access():
	publicKey = request.headers.get( "PublicKey", None )
	if publicKey:
		user = _security.datastore.find_user( email=publicKey )

		if user:
			privateKey = user.password

			body = request.form.get( "data", None )

			if not body:
				body = {}
			else:
				body = current_app.json_decoder.decode( body )

			signature = _calc_signature( privateKey, publicKey, request.path, body )

			if signature == request.headers.get( "Signature", "" ):
				return True
			else:
				return False
	else:
		return False

def _check_timestamp():
	timestamp = request.headers.get( "Timestamp", None )

	if timestamp:
		timestamp = int( timestamp )
		currentTimestamp = time.time()

		if timestamp >= currentTimestamp - 300:
			return True
		else:
			return False
	else:
		return False

parser = reqparse.RequestParser()
parser.add_argument( "Timestamp", type=int, required=True, help="Timestamp must be an integer value." )
parser.add_argument( "Signature", type=str, required=True, help="Signature must be a string value." )
parser.add_argument( "PublicKey", type=str, required=True, help="PublicKey must be a string value." )
def secure( f ):
	"""
		This will wrap a method that will then check if the passed in
		credentials are correct else it will throw a error and cause
		a 401 message. If the credentials are correct BUT the user
		does not have the proper role to access the information then
		a 404 message will be thrown to hide information.

		The auth is similar to the AWS authorization.

		There is a public and a private key.

		The public key shall be a random byte string stored in b64
		of length 128.
		The private key shall be a random byte string stored in b64
		of length 512.

		The following headers will be used.

		Signature -> Shall be the Sha512 of the following:
				<private key>|<action>|<public key>|<url encoded list of body>
		Timestamp -> The current time stamp of the request. To be valid
				it must be within the past 5 minutes.
		PublicKey -> The public key of the requesting client.

	"""
	@wraps( f )
	def wrapped( *args, **kwargs ):
		parser.parse_args()
		if _check_access() and _check_timestamp():
			return f( args, kwargs )
		else:
			return False
	
	return wrapped

def secure_unauthorized():
	return { "message": "Information was not found.", "status": 404 }, 404
