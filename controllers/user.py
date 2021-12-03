from flask import request
from flask_restplus import Resource, fields

from models.user import UserModel
from schemas.user import UserSchema

from server.instance import server

user_schema = UserSchema()

class User(Resource):
    
    def get(self, id):
        user_data = UserModel.find_by_id(id)
        if user_data:
            return user_schema.dump(user_data)
