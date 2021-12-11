from db import db

class CourseModel(db.Model):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    # description = db.Column(db.String(200))
    users = db.relationship("UserModel")

    def __init__(self, name):
        self.name = name
        # self.description = description

    def json(self):
        return {
            "name": self.name,
            "description": self.description
        }
        
    def __repr__(self):
        return f'CourseModel(name={self.name})'

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
