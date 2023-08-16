from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id_user = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    # posts_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    # posts = db.relationship("Post")
    # comments_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    # comments = db.relationship("Comments")

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "userid": self.id,
            "name": self.name,
            "lastName": self.last_name,
            "email": self.email,
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
    name = db.Column(db.String(100), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet = db.relationship("Planets")  
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character = db.relationship("Characters")  
    starship_id = db.Column(db.Integer, db.ForeignKey('starships.id'))
    starship = db.relationship("StarShips") 

    def __repr__(self):
        return '<Favorites %r>' % self.user_id

    def serialize(self):
        return {
            "userid": self.user_id,
            "name": self.name,
            "planet": self.planet_id,
            "character": self.character_id,
            "starship": self.starship_id
        }
# class Post(db.Model):
#     __tablename__ = 'posts'
#     id = db.Column(db.Integer, primary_key=True)
#     body_post = db.Column(db.String(250), nullable=True)
#     name_post = db.Column(db.String(50), nullable=True)

#     def __repr__(self):
#         return '<Post %r>' % self.posts.id

#     def serialize(self):
#         return {
#             "posts_id": self.posts.id,
#             "body_post": self.body,
#         }

# class Comments(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)

#     body_comment = db.Column(db.String(250), nullable=True)
#     name_comment = db.Column(db.String(50), nullable=True)

#     def __repr__(self):
#         return '<Comments %r>' % self.comments.id

#     def serialize(self):
#         return {
#             "comments_id": self.comments.id,
#             "body_comment": self.body
#         }

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    rotation_period = db.Column(db.String(50), nullable=True)
    diameter = db.Column(db.String(50), nullable=True)
    terrain = db.Column(db.String(50), nullable=True)
    population = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(200), nullable=True)
    

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
            "terrain": self.terrain,
            "population": self.population,
            "climate": self.climate,
        }
    

class StarShips(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    model = db.Column(String(20))
    starship_class = db.Column(String(20), nullable=True)
    manufacturer = db.Column(String(20), nullable=True)
    cost_in_credits = db.Column(Integer, nullable=True)
    crew = db.Column(Integer, nullable=True)
    passengers = db.Column(Integer, nullable=True)
    max_atmosphering_speed = db.Column(Integer, nullable=True)
    hyperdrive_rating = db.Column(Integer, nullable=True)
    cargo_capacity = db.Column(Integer, nullable=True)
    consumables = db.Column(String(20), nullable=True)
    pilots = db.Column(String(20), nullable=True)
    name = db.Column(String(20), nullable=True)
    

    def __repr__(self):
        return '<StarShips %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "pilots": self.pilots,
            "created": self.created,
            "name": self.name,
        }

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    height = db.Column(db.String(50), nullable=True)
    hair_color = db.Column(db.String(50), nullable=True)
    eye_color = db.Column(db.String(20), nullable=True)
    birth_year = db.Column(db.String(20), nullable=True)
    gender = db.Column(db.String(50), nullable=True)
    

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }




