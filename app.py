from player_search import search_player
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    player_name = request.form['player_name']
    
    #Making the actual search
    search_results = search_player(player_name)
    
    return jsonify(search_results)

if __name__ == '__main__':
    app.run(debug=True)