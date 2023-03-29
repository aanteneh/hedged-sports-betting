import scraping
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

dkUrl = "https://sportsbook.draftkings.com/leagues/basketball/88670846"  # DraftKings

dkReq = Request(dkUrl, headers=scraping.hdr)
dkPage = urlopen(dkReq)
dkSoup = BeautifulSoup(dkPage, features="html.parser")

dkteamContent = dkSoup.find_all(
    'div', attrs={'class': 'event-cell__name-text'})
dkoddsContent = dkSoup.find_all(
    'span', attrs={'class': 'sportsbook-odds american no-margin default-color'})

# initialize storage arrays
dkTeams = []
dkOdds = []

dkTeams = scraping.get_names(dkteamContent)
dkOdds = scraping.get_odds(dkoddsContent)

draftKingsdf = scraping.store_data(dkTeams, dkOdds)
print(draftKingsdf)