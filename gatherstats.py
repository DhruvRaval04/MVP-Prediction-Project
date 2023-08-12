from import_requests import WebScraper
import requests
from bs4 import BeautifulSoup as bs
import csv
import re
import lxml
import pandas as pd
ws = WebScraper()
year = 1960
i = 0
while (year!=2010):
    
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html#per_game_stats::pts_per_g"
    WebScraper.create_csv(url)
    year = year + 1
    i = i+1


