from player_search import search_player
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        player_name = request.form.get('player_name')
        if not player_name:
            return jsonify({'error': 'Player name not provided'}), 400
        
        # Making the actual search
        search_results = search_player(player_name)
        
        # Return search results as JSON
        return jsonify(search_results)
    
    # Render the HTML file for GET request
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)