from flask import Blueprint, request, jsonify
from app import db
from app.models import Movie, Actor

movies_bp = Blueprint('movies', __name__)

# GET all movies with pagination and custom filters
@movies_bp.route('/movies', methods=['GET'])
def get_movies():
    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Custom filters
    actor_name = request.args.get('actor_name')
    director_name = request.args.get('director_name')

    query = Movie.query

    if actor_name:
        query = query.filter(Movie.actors.any(name=actor_name))
    if director_name:
        query = query.filter(Movie.director == director_name)

    movies = query.paginate(page=page, per_page=per_page)
    
    return jsonify([movie.serialize() for movie in movies.items]), 200

# GET a specific movie by ID
@movies_bp.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get_or_404(id)
    return jsonify(movie.serialize()), 200

# POST a new movie
@movies_bp.route('/movies', methods=['POST'])
def add_movie():
    data = request.json
    new_movie = Movie(name=data['name'], year=data['year'], ratings=data['ratings'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify(new_movie.serialize()), 201

# POST update a movie by ID
@movies_bp.route('/movies/<int:id>', methods=['POST'])
def update_movie(id):
    movie = Movie.query.get_or_404(id)
    data = request.json
    movie.name = data.get('name', movie.name)
    movie.year = data.get('year', movie.year)
    movie.ratings = data.get('ratings', movie.ratings)
    db.session.commit()
    return jsonify(movie.serialize()), 200

# POST delete an actor by ID if not associated with any movies
@movies_bp.route('/actors/<int:id>', methods=['POST'])
def delete_actor(id):
    actor = Actor.query.get_or_404(id)
    associated_movies = Movie.query.filter(Movie.actors.any(id=id)).all()
    if not associated_movies:
        db.session.delete(actor)
        db.session.commit()
        return jsonify(message="Actor deleted successfully"), 200
    else:
        return jsonify(message="Actor is associated with movies and cannot be deleted"), 400
