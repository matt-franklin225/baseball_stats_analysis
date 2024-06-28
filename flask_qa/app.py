from player_search import search_player
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#@app.route('/search', methods=['POST'])
@app.route('/')
def home():
    player_name = request.form['player_name']
    
    #Making the actual search
    search_results = search_player(player_name)
    
    #return jsonify(search_results)
    return 'Drink tea'

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80, debug=True)