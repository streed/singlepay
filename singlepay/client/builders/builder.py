
class BuilderMetaClass( type ):

	__attribute_name = "_attributes_"

	def __init__( self, name, bases, dct ):
		type.__init__( self, name, bases, dct )

		if BuilderMetaClass.__attribute_name in dct:
			for k in self._attributes_:
				def temporary_function( s, value, _k=k ):
					setattr( s._instance, "_%s" % _k, value )
					return s
				setattr( self, "set_%s" % k, temporary_function )
		

class Builder( object ):
	__metaclass__ = BuilderMetaClass

	def __init__( self, api ):
		self._api = api
	
	def create( self ):
		self._instance = self._model_( self._api )

		for k in self._attributes_:
			getattr( self, "set_%s" % k )( self._attributes_[k] )
		return self

	def finalize( self ):
		self._instance._finalize()
		return self._instance

	def find( self ):
		self.finalize()
		return self._instance.find()
	
	def save( self ):
		self.finalize()
		return self._instance.save()

