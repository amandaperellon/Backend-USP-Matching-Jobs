from db import db
from passlib.hash import sha256_crypt


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(45), nullable=False)
    birthdate = db.Column(db.Date)
    is_admin = db.Column(db.Boolean)
    profile_img_path = db.Column(db.String(200))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    ocupation_id = db.Column(db.Integer, db.ForeignKey('occupations.id'))


    def __init__(self, name, username, password, birthdate, admin, profile_img_path):
        self.name = name
        self.username = username
        self.password = sha256_crypt().encrypt(password)
        self.birthdate = birthdate
        self.admin = admin
        self.profile_img_path = profile_img_path

    def json(self):
        return {
            "name": self.name,
            "username": self.username,
            "birthdate": self.birthdate,
            "is_admin": self.is_admin,
            "profile_img_path": self.profile_img_path
        }
        
    def __repr__(self):
        return f'UserModel(name={self.name}, username={self.username})'

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
        
