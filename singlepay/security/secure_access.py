from flask.ext.security import login_required

def secure( f ):
	"""
		This will wrap a method that will then check if the passed in
		credentials are correct else it will throw a error and cause
		a 401 message. If the credentials are correct BUT the user
		does not have the proper role to access the information then
		a 404 message will be thrown to hide information.
	"""
	return login_required( f )

def secure_unauthorized():
	return { "message": "Information was not found.", "status": 404 }, 404
