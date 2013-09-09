
class BuilderMetaClass( type ):

	__attribute_name = "_attributes_"

	def __init__( self, name, bases, dct ):
		type.__init__( self, name, bases, dct )

		if BuilderMetaClass.__attribute_name in dct:
			for k in self._attributes_:
				def temporary_function( s, value ):
					setattr( s._instance, "_%s" % k, value )
					return s

				setattr( self, "set_%s" % k, temporary_function )
		
			def create( s ):
				s._instance = s._model_( s._api )

				#Set all the defaults on the object
				for k in s._attributes_:
					getattr( s, "set_%s" % k )( self._attributes_[k] )

				return s

			setattr( self, "create", create )

			def finalize( s ):
				s._instance._finalize()

				return s._instance

			setattr( self, "finalize", finalize )


class Builder( object ):
	__metaclass__ = BuilderMetaClass

	def __init__( self, api ):
		self._api = api
