from typing import List, Dict

#import pandas
from flask import jsonify
from db import fifa_df


def get_players_by_team(club: str, national: str = "None") -> List[Dict]:
    if national != "None":
        filtered_data = fifa_df.query(f"Club == '{club}' & Nationality == '{national}'")
    else:
        filtered_data = fifa_df.query(f"Club == '{club}'")
    res = []
    res.extend(list(filtered_data.to_dict("records")))
    return res


def get_player_details(player: str) -> List[Dict]:
    filtered_data = fifa_df.query(f"Name == '{player}'")
    res = []
    res.extend(list(filtered_data.to_dict("index").values()))
    return res
