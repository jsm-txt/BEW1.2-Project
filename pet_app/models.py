from sqlalchemy_utils import URLType
from flask_login import UserMixin
from sqlalchemy.orm import backref
from pet_app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f'<User: {self.username}>'

class Pet(db.Model):
    __tablename__='pet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    photo_url = db.Column(URLType)
    pet_images = db.relationship('Image', back_populates='images_of')
    def __repr__(self):
        return f'Pet: {self.name}'
    def __str__(self):
        return f'Pet: {self.name}'

class Image(db.Model):
    __tablename__='images'
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(80), nullable=False)
    photo_url = db.Column(URLType)
    pet_id = db.Column(
        db.Integer, db.ForeignKey('pet.id'), nullable=False)
    images_of = db.relationship('Pet', back_populates='pet_images')
    def __repr__(self):
        return f'Caption: {self.caption}'
    def __str__(self):
        return f'Caption: {self.caption}'
