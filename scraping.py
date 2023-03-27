# Scraping Method from SportsBetting.ag site

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

dkUrl = "https://sportsbook.draftkings.com/leagues/basketball/88670846"  # DraftKings
fdUrl = "https://sportsbook.fanduel.com/navigation/nba"  # FanDuel

# for some reason have to follow this request convention
hdr = {'User-Agent': 'Mozilla/5.0'}
dkReq = Request(dkUrl, headers=hdr)
dkPage = urlopen(dkReq)
fdReq = Request(fdUrl, headers=hdr)
fdPage = urlopen(fdReq)

dkSoup = BeautifulSoup(dkPage, features="html.parser")
fdSoup = BeautifulSoup(fdPage, features="html.parser")

dkteamContent = dkSoup.find_all(
    'div', attrs={'class': 'event-cell__name-text'})
dkoddsContent = dkSoup.find_all(
    'span', attrs={'class': 'sportsbook-odds american no-margin default-color'})

fdteamContent = fdSoup.find_all(
    'span', attrs={'class': 's t if ig ih ii ho hp hq hu ij h ep dp ik bd'})
fdoddsContent = fdSoup.find_all(
    'span', attrs={'class': 'im in ep ej iw ix fg'})

print(fdteamContent)


# initialize storage arrays
dkTeams = []
dkOdds = []
fdTeams = []
fdOdds = []

# def convert_units(content):
#     arr = []
#     for i in range(len(content)):
#         if (int(content[i]) >= 0):
#             arr.append(int(content[i]) / (100+1))
#         else:
#             arr.append(1 - (100 / int(content[i])))
#     return arr


def get_names(content):
    arr = []
    for frame in content:
        arr.append(frame.getText().replace(
            '\n', '').replace('\t', '').replace(' ', ''))
    return arr


def get_odds(content):
    arr = []
    for frame in content:
        arr.append(frame.getText().replace('\n', '').replace('\t', ''))
    return arr


dkTeams = get_names(dkteamContent)
dkOdds = get_odds(dkoddsContent)
