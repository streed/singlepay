from ..app import db
from flask.ext.security import UserMixin, RoleMixin

api_roles_users = db.Table( "api_roles_users", db.Column( "apiuser_id", db.Integer(), db.ForeignKey( "api_user.id" ) ),
					       db.Column( "apirole_id", db.Integer(), db.ForeignKey( "api_role.id" ) ) )

class ApiRole( db.Model, RoleMixin ):
	id = db.Column( db.Integer(), primary_key=True )
	name = db.Column( db.String( 80 ), unique=True )
	description = db.Column( db.String( 255 ) )

class ApiUser( db.Model, UserMixin ):
	id = db.Column( db.Integer(), primary_key=True )
	active = db.Column( db.Boolean() )
	email = db.Column( db.String( 64 ), unique=True )
	password = db.Column( db.String( 128 ) )
	last_login_at = db.Column( db.DateTime() )
	current_login_at = db.Column( db.DateTime() )
	last_login_ip = db.Column( db.String( 64 ) )
	current_login_ip = db.Column( db.String( 64 ) )
	login_count =  db.Column( db.Integer() )

	roles = db.relationship( "ApiRole", secondary=api_roles_users, backref=db.backref( "apiusers", lazy="dynamic" ) )
