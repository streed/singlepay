
class SinglePayError( Exception ):
	pass

class SinglePayPermissionsError( SinglePayError ):
	def __init__( self, resource ):
		message = "You do not have the proper permissions to access %s" % resource

		Exception.__init__( self, message )

class SinglePayInvalidMethodError( SinglePayError ):
	def __init__( self, method ):
		message = "Invalid Method: %s" % method

		Exception.__init__( self, messge )
