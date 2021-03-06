from db import db

class OccupationModel(db.Model):
    __tablename__ = "occupations"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    users = db.relationship("UserModel")

    def json(self):
        return {
            "name": self.name,
        }
        
    def __repr__(self):
        return f'OccupationModel(name={self.name})'

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
