import os

from pandas import read_csv

fifa_df = read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "players_fifa22.csv"))