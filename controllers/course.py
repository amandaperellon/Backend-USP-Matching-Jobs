from flask import request
from flask_restplus import Resource, fields

from models.course import CourseModel
from schemas.course import CourseSchema

from server.instance import server

course_schema = CourseModel()

class Course(Resource):
    
    def get(self, id):
        course_data = CourseModel.find_by_id(id)
        if course_data:
            return course_schema.dump(course_data)
