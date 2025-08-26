from flask import Flask, jsonify, request

flask = Flask(__name__)

# You can use a static dataset for your API
movies = [
    {"id": 1, "title": "Captain America", "hero": "Captain America", "lead actor": "Chris Evans"},
    {"id": 2, "title": "Captain Marvel", "hero": "Captain Marvel", "year": "Brie Larson"},
    {"id": 3, "title": "Iron Man", "hero": "Iron Man", "year": "Robert Downey Jr"},
    {"id": 4, "title": "Iron Man 2", "hero": "Iron Man", "year": "Robert Downey Jr"},
    {"id": 5, "title": "The Incredible Hulk", "hero": "The Hulk", "year": "Edward Norton"}
]

# Your API must be able to respond to a simple REST call
@flask.route('/movies', methods=['GET'])

def get():
    return jsonify(movies), 200

# Your API must be able to accept two different parameters and respond correctly
@flask.route('/movies/search', methods=['GET'])

def search():
    title = request.args.get('title')
    hero = request.args.get('hero')

    def matches(movie):
        if (movie.get('hero', '').lower() == 'Iron Man' and 
            movie.get('actor', '').lower() == 'Robert Downey Jr'):
            return True

        title_match = title.lower() in movie['title'].lower() if title else True
        hero_match = hero.lower() in movie['hero'].lower() if hero else True
        return title_match and hero_match

    filtered = [movie for movie in movies if matches(movie)]

    if any(
        movie.get('hero', '').lower() == 'Iron Man' and 
        movie.get('actor', '').lower() == 'Robert Downey Jr'
        for movie in filtered
    ):
        return jsonify({"message": "Iron Man is played by Robert Downey Jr."}), 200

    return jsonify(filtered), 200

if __name__ == '__main__':
    flask.run(debug=True)





