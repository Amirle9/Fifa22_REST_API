Installation

- pip install -r requirements.txt
- python main.py

After executing these commands, we can reach our application by opening the URL http://127.0.0.1:5000/ at your browser.

API

1. Get list of players by team- 
  Navigate to http://127.0.0.1:5000/club/<name_of_team>.  
  For example, in order to get a list of Arsenal players, you should navigate to:
  http://127.0.0.1:5000/club/Arsenal .

2.  Get list of players by team filtered by nationality-
Navigate to http://127.0.0.1:5000/club/<name_of_team>/<nationality>.  
For example, in order to get a list of french players who play at Chelsea, you should navigate to: http://127.0.0.1:5000/club/Chelsea/France .  

3. Get player details-
Navigate to http://127.0.0.1:5000/player/<name_of_player>.
For example, in order to get details about a specific player, you should navigate to: http://127.0.0.1:5000/player/<name_of_player> .  
In order to get some details about Messi, you should navigate to: http://127.0.0.1:5000/player/L. Messi .
