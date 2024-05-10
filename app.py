from player_search import search_player
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    player_name = request.form['player_name']
    
    # Here you would call your Python script to perform the search
    # Replace this with your actual script execution
    search_results = search_player(player_name)
    
    return jsonify(search_results)

if __name__ == '__main__':
    app.run(debug=True)