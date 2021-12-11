from flask import request
from flask_restplus import Resource, fields
from passlib.hash import sha256_crypt
from datetime import datetime, timedelta
import jwt

from models.user import UserModel
from schemas.user import UserSchema

from server.instance import server

user_schema = UserSchema()
user_list_schema = UserSchema(many=True)

class User(Resource):
    
    def get(self, id):
        user_data = UserModel.find_by_id(id)
        if user_data:
            unfiltered_data = user_schema.dump(user_data)

            filtered_data = {}
            filtered_data['id'] = unfiltered_data['id']
            filtered_data['name'] = unfiltered_data['name']
            filtered_data['username'] = unfiltered_data['username']
            filtered_data['email'] = unfiltered_data['email']
            return filtered_data



class UserList(Resource):

    def get(self):
        user_data = UserModel.find_all()
        if user_data:
            unfiltered_data = user_list_schema.dump(user_data)

            filtered_data = []

            for user in unfiltered_data:
                filtered_data.append({
                    'id': user['id'],
                    'name': user['name'],
                    'username': user['username'],
                    'email': user['email']
                })

            return filtered_data

    def post(self):
        user_json = request.form.to_dict()
        user_data = user_schema.load(user_json)

        user_data.save_to_db()

        unfiltered_data = user_schema.dump(user_data)

        filtered_data = {}
        filtered_data['id'] = unfiltered_data['id']
        filtered_data['name'] = unfiltered_data['name']
        filtered_data['username'] = unfiltered_data['username']
        filtered_data['email'] = unfiltered_data['email']

        return filtered_data, 200

class Session(Resource):
    def post(self):
        user_json = request.get_json()
        user_data = UserModel.find_by_username(user_json['username'])
        if user_data:
            is_authenticated = sha256_crypt.verify(user_json['password'], user_data.password)

            token = jwt.encode({
                'id': user_data.id,
                'exp': datetime.utcnow() + timedelta(minutes=30)
            }, server.app.config['SECRET_KEY'])

            return {'token': token}, 200


        else:
            return {'error': 'No usr found with this username'}, 404


