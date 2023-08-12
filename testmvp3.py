from import_requests import WebScraper
import requests
from bs4 import BeautifulSoup as bs
import csv
import re
import lxml
import pandas as pd
ws = WebScraper()
yeargap = 10
year = 2010
w, h = 2, 10
mvplist = [[0 for x in range(w)] for y in range(h)] 
i = 0
while (year!=2020):
    mvpurl = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + ".html"

    mvp = WebScraper.mvp(mvpurl) 
    mvplist[i][0] = year
    mvplist[i][1] = mvp
    year = year + 1
    i = i+1

headings = ["Year", "MVP"]
##makes a csv with all mvps and corresponding years 
with open(("testmvp.csv"), "w",  encoding="utf-8") as f:
    wr = csv.writer(f,delimiter=',')
    wr.writerow(headings)
    wr.writerows(mvplist)