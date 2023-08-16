"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favorites, Planets, StarShips, Characters
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
# desde aqui empiezo 
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# Favorites

@app.route('/favorites/<int:favorites_id>', methods=['GET', 'POST'])
def manage_favorites(favorites_id):
    if request.method == 'GET':
        favorites = Favorite.query.filter_by(user_id=favorites_id).all()
        serialized_favorites = [{'id': fav.id, 'favorite_name': fav.favorite_name} for fav in favorites]
        return jsonify(serialized_favorites), 200
    
    if request.method == 'POST':
        body = request.get_json()  # Input: {'favorite_name': 'favorite_item_name'}
        new_favorite = Favorite(user_id=favorites_id, favorite_name=body.get('favorite_name'))
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({"message": "Favorite added successfully"}), 201
    
    return "Invalid Method", 405


# Characters
@app.route('/characters', methods=['GET'])
def handle_all_characters():

    characters = Characters.query.all()
    serialized_characters = [character.serialize() for character in characters]

    response_body = {
        "characters": serialized_characters,
        "msg": "Hello, esto es tu GET de todos los /Characters y responde "
        
    }

    return jsonify(response_body), 200


@app.route('/characters/<int:character_id>', methods=['GET'])
def get_single_character(character_id):

    character = Characters.query.get(character_id)
    if character is None:
        return "Character not found, este personaje no existe menda", 404

    return jsonify(character.serialize()), 200


# Planets
@app.route('/planets', methods=['GET'])
def handle_planets():

    planets = Planets.query.all()
    serialized_planets = [planet.serialize() for planet in planets]

    response_body = {
        "planets": serialized_planets,
        "msg": "Hello, this is your GET /Planets response "
        
    }

    return jsonify(response_body), 200


@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_single_planet(planet_id):

    planet = Planets.query.get(planet_id)
    if planet is None:
        return "Planet not found, este planeta no existe menda", 404

    return jsonify(planet.serialize()), 200


# StarShips
@app.route('/starships', methods=['GET'])
def handle_all_starships():

    starships = Starships.query.all()
    serialized_starships = [starship.serialize() for starship in starships]

    response_body = {
        "starships": serialized_starships,
        "msg": "Hello, esto es el GET  de todas /Starships responde "
    }

    return jsonify(response_body), 200


@app.route('/starships/<int:starships_id>', methods=['GET'])
def get_single_starship(starships_id):

    starship = Starships.query.get(starships_id)
    if starship is None:
        return "starship not found, esta nave no existe menda", 404

    return jsonify(starship.serialize()), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
