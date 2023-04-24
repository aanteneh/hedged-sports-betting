import scraping
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

agUrl = "https://www.sportsbetting.ag/sportsbook/basketball/nba"  # AgBets

agReq = Request(agUrl, headers=scraping.hdr)
agPage = urlopen(agReq)
agSoup = BeautifulSoup(agPage, features="html.parser")

agTeamContent = agSoup.find_all('td', attrs={'class': 'col_teamname bdevtt'})
agOddsContent = agSoup.find_all(
    'td', attrs={'class': 'odds bdevtt moneylineodds displayOdds'})

agTeams = []
agOdds = []

agTeams = scraping.get_names(agTeamContent)
agAmOdds = scraping.get_odds(agOddsContent)

# agOdds = scraping.convert_units(agAmOdds)

agDf = scraping.store_data(agTeams, agAmOdds)
