from init import db,ma

class User(db.Model): #Gets data from database
    __tablename__ = 'users'
    # attributes freom draw.io
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)    
    is_admin = db.Column(db.Boolean, default=False)
    
class UserSchema(ma.Schema):  #converts to JSON
    class Meta: 
        fields = ('id', 'name', 'email', 'password', 'is_admin') #fields being converted
        
user_schema = UserSchema(exclude=['password']) # retrieves single user, excluding password
users_schema = UserSchema(many=True, exclude=['password'])# list of users