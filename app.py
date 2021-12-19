from flask import Flask, jsonify
from db.db_functions import get_players_by_team, get_player_details

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['JSON_AS_ASCII'] = False


@app.route('/club/<string:club>', defaults={'national': "None"})
@app.route("/club/<string:club>/<string:national>")
def get_by_team(club: str, national: str):
    return jsonify(get_players_by_team(club, national))


@app.route("/player/<string:player>")
def get_by_player(player: str):
    return jsonify(get_player_details(player))


if __name__ == '__main__':
    app.run(debug=True)
