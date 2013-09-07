from flask.ext import restful

from ..security.secure_access import secure

class SecureResource( restful.Resource ):

	decorators = [ secure ]
