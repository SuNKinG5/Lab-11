# นายตะวัน อุตมาน 663380210-2 Sec.1

from flask import Flask, request
from flask_restful import Resource, Api
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

movies_data = [
    {"playlist_id":1, "playlist_name":"datenight", "movie_list":["The Notebook", "50 First Dates", "A Walk to Remember"]},
    {"playlist_id":2, "playlist_name":"action", "movie_list":["Die Hard", "Mad Max: Fury Road", "John Wick"]},
    {"playlist_id":3, "playlist_name":"comedy", "movie_list":["Superbad", "Step Brothers", "The Hangover"]},
]

class Movies(Resource):
    def get(self):
        """ 
        Get a list of all playlist 
        ---
        responses:
          200:
            description: A list of Playlists
        """
        return movies_data, 200

    def post(self):
        """
        Create a new playlist
        ---
        parameters:
          - in: body
            name: Playlist
            required: true
            schema: 
                playlist_id: Playlist 
                required:
                    - name 
                properties: 
                    name: 
                        type: string 
                        description: The name of the playlist 
                    movies: 
                        type: list 
                        description: The list of the movies
        responses:
            201:
                description: A new playlist created
            400:
                description: Bad request
        """
        new_id = movies_data[-1]['playlist_id'] + 1
        data = request.get_json()       # retrieves the JSON data from the request object
        new_playlist = {'playlist_id': new_id, 'playlist_name': data['name'], 'movie_list': data['movies']}
        movies_data.append(new_playlist)
        return new_playlist, 201
    
    
# Routes 
api.add_resource(Movies, '/playlists')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
    
    