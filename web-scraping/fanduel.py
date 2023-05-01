# NOT BEING USED!!

import scraping
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

fdUrl = "https://sportsbook.fanduel.com/navigation/nba"  # FanDuel

fdReq = Request(fdUrl, headers=scraping.hdr)
fdPage = urlopen(fdReq)
fdSoup = BeautifulSoup(fdPage, features="html.parser")

fdteamContent = fdSoup.find_all(
    'span', attrs={'class': 's t if ig ih ii ho hp hq hu ij h ep dp ik bd'})
fdoddsContent = fdSoup.find_all(
    'span', attrs={'class': 'im in ep ej iw ix fg'})


# initialize storage arrays
fdTeams = []
fdOdds = []

fdTeams = scraping.get_names(fdteamContent)
fdOdds = scraping.get_odds(fdoddsContent)
