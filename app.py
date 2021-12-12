from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from ma import ma
from db import db

from marshmallow import ValidationError

from server.instance import server

from controllers.user import User, UserList, Session
from controllers.course import Course
from controllers.occupation import Occupation

api = server.api
app = server.app


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(User, '/users/<int:id>')
api.add_resource(UserList, '/users')
api.add_resource(Session, '/session')
api.add_resource(Course, '/courses/<int:id>')
api.add_resource(Occupation, '/occupations/<int:id>')


db.init_app(app)
ma.init_app(app)
if __name__ == '__main__':
    server.run()
