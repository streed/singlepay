import hashlib
import time
from functools import wraps
from flask import current_app, request, _request_ctx_stack
from flask.ext.security import login_required
from flask.ext.restful import reqparse
from flask.ext.principal import Identity, identity_changed
from werkzeug.local import LocalProxy

try:
	from urllib.parse import quote
except ImportError:
	from urllib import quote

#Grab a thread local proxy to the security extension.
_security = LocalProxy( lambda: current_app.extensions["security"] )


def _calc_signature( private, public, action, body, timestamp ):
	"""
		This will take the private, public, action, body, timestamp
		and construct the proper signature for use in verification
		of the request.
	"""
	signature = "%s|%s|%s|%d|" % ( private, action, public, timestamp )

	keys = sorted( body.keys() )

	body_strs = []
	for k in keys:
		body_strs.append( "%s=%s" % ( quote( k, safe='' ), quote( body[k], safe="-_~" ) ) )

	signature += "&".join( body_strs )

	sig = hashlib.sha512()
	sig.update( signature )

	return sig.hexdigest().strip().encode( "utf-8" )

def _check_access():
	"""
		This will get the publicKey, timestamp, body, and the path
		and verify that the Signature in the header is correct. 
		It will also make sure that the request is not over 5mins old.

		If the request is valid then the current user is set to the right
		user and True is returned, else False is returned.
	"""
	publicKey = request.headers.get( "PublicKey", None )
	timestamp = request.headers.get( "Timestamp", None )
	user = _security.datastore.find_user( email=publicKey )

	if user and user.is_active():
		privateKey = user.password

		body = request.form.get( "data", None )

		if not body:
			body = {}
		else:
			body = current_app.json_decoder.decode( body )

		timestamp = int( timestamp )
		signature = _calc_signature( privateKey, publicKey, request.path, body, timestamp )
		currentTimestamp = time.time()

		if ( signature == request.headers.get( "Signature", "" ) ) and ( timestamp >= currentTimestamp - 300 ):
			app = current_app._get_current_object()
			_request_ctx_stack.top.user = user
			identity_changed.send( app, identity=Identity( user.id ) )
			return True
		else:
			return False
	else:
		return False

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

		TODO: MAKE SURE THAT THE HEADERS ARE TEHRE AND IN THE PROPER FORMAT.
	"""
	@wraps( f )
	def wrapped( *args, **kwargs ):
		if _check_access():
			return f( *args, **kwargs )
		else:
			return secure_unauthorized()
	
	return wrapped

def secure_unauthorized():
	return { "message": "Information was not found.", "status": 404 }, 404
