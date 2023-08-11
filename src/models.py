from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }

class User(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    lastName = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    favorites = relationship("Favorites", back_populates="user")
    posts = relationship("Post", back_populates="user")
    comments = relationship("Comments", back_populates="user")

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "userid": self.userid,
            "name": self.name,
            "lastName": self.lastName,
            "email": self.email,

            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, ForeignKey('user.userid'))
    name = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250))
    user = relationship("User", back_populates="favorites")
    planet = relationship("Planets.id", back_populates="favorites")
    character = relationship("Characters", back_populates="favorites")
    starship = relationship("StarShips", back_populates="favorites")

    def __repr__(self):
        return '<Favorites %r>' % self.userid

    def serialize(self):
        return {
            "userid": self.userid,
            "name": self.name,
            "email": self.email,
            "planet": self.planet,
            "character": self.character,
            "starship": self.starship
            # do not serialize the password, its a security breach
        }
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, ForeignKey('user.userid'))
    body = db.Column(db.String(250))
    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return '<Post %r>' % self.userid

    def serialize(self):
        return {
            "userid": self.userid,
            "body": self.body,
            # do not serialize the password, its a security breach
        }

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, ForeignKey('user.userid'))
    body = db.Column(String(250))
    user = relationship("User", back_populates="comments")

    def __repr__(self):
        return '<Comments %r>' % self.userid

    def serialize(self):
        return {
            "userid": self.userid,
            "body": self.body
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    planetid = db.Column(db.Integer, primary_key=True)
    characteristics = db.Column(db.String, nullable=False)
    favorites = relationship("Favorites", back_populates="planet")

    def __repr__(self):
        return '<Planets %r>' % self.userid

    def serialize(self):
        return {
            "planetid": self.planetid,
            "characteristics": self.characteristics
            # do not serialize the password, its a security breach
        }
    

class StarShips(db.Model):
    __tablename__ = 'starships'
    starshipsid = db.Column(db.Integer, primary_key=True)
    characteristics = db.Column(db.String, nullable=False)
    favorites = relationship("Favorites", back_populates="starship")

    def __repr__(self):
        return '<StarShips %r>' % self.userid

    def serialize(self):
        return {
            "starshipsid": self.starshipsid,
            "characteristics": self.characteristics,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    charactersid = db.Column(db.String, primary_key=True)
    characteristics = db.Column(db.String, nullable=False)
    favorites = relationship("Favorites", back_populates="character")

    def __repr__(self):
        return '<Characters %r>' % self.userid

    def serialize(self):
        return {
            "charactersid": self.charactersid,
            "characteristics": self.characteristics,
            # do not serialize the password, its a security breach
        }

class PlanetsDetails(db.Model):
    __tablename__ = 'planetsdetails'
    planetid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    planet = relationship("Planets", back_populates="planetsdetails")

    def __repr__(self):
        return '<PlanetsDetails %r>' % self.userid

    def serialize(self):
        return {
            "planetid": self.planetid,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class StarShipsDetails(db.Model):
    __tablename__ = 'starshipsdetails'
    starshipid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    starship = relationship("StarShips", back_populates="starshipsdetails")

    def __repr__(self):
        return '<StarShipsDetails %r>' % self.userid

    def serialize(self):
        return {
            "starshipid": self.starshipid,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class CharactersDetails(db.Model):
    __tablename__ = 'charactersdetails'
    characterid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    character = relationship("Characters", back_populates="charactersdetails")

    def __repr__(self):
        return '<CharactersDetails %r>' % self.characterid

    def serialize(self):
        return {
            "characterid": self.characterid,
            "name": self.name,
            # do not serialize the password, its a security breach
        }