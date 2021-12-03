from ma import ma
from models.user import UserModel

class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True

