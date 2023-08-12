from import_requests import WebScraper
import requests
from bs4 import BeautifulSoup as bs
import csv
import re
import lxml
import pandas as pd
ws = WebScraper()
yeargap = 50
year = 1960
w, h = 2, 50
mvplist = [[0 for x in range(w)] for y in range(h)] 
i = 0
while (year!=2010):
    ##check out test and gather stats
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html#per_game_stats::pts_per_g"
    ##WebScraper.create_csv(url)

    mvpurl = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + ".html"

    mvp = WebScraper.mvp(mvpurl) 
    mvplist[i][0] = year
    mvplist[i][1] = mvp

    ##team record cannot scrape due to inteference with firewall
    masterlist = WebScraper.teamrecordsetup(url)
    for i in range(20):
        masterlist[i][2]= WebScraper.teamrecordnum("https://www.basketball-reference.com/teams/" + masterlist[i][1] + "/" + str(year) + ".html")
        
        ##putting it into a csv file 
    with open((str(year) + " teamrecord.csv"), "w",  encoding="utf-8") as f:
        wr = csv.writer(f,delimiter=',')
        wr.writerows(masterlist)
    
    year = year + 1
    i = i+1

headings = ["Year", "MVP"]
##makes a csv with all mvps and corresponding years 
with open(("mvp2.csv"), "w",  encoding="utf-8") as f:
    wr = csv.writer(f,delimiter=',')
    wr.writerow(headings)
    wr.writerows(mvplist)


 
