from flask import request
from flask_restplus import Resource, fields

from models.occupation import OccupationModel
from schemas.occupation import OccupationSchema

from server.instance import server

occupation_schema = OccupationSchema()

class Occupation(Resource):
    
    def get(self, id):
        occupation_data = OccupationModel.find_by_id(id)
        if occupation_data:
            return occupation_schema.dump(occupation_data)
