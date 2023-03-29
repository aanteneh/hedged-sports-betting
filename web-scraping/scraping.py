# Scraping Method general file

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# for some reason have to follow this request convention
hdr = {'User-Agent': 'Mozilla/5.0'}


def convert_units(content):
    arr = []
    for i in range(len(content)):
        if (int(content[i]) >= 0):
            arr.append(int(content[i]) / (100+1))
        else:
            arr.append(1 - (100 / int(content[i])))
    return arr


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


def store_data(teams, odds):
    arr = []
    for i in range(len(teams), 2):
        r = []
        r.append(teams[i])
        r.append(teams[i+1])
        r.append(odds[i])
        r.append(odds[i+1])
        arr.append(r)
    return pd.DataFrame(columns=['Team 1', 'Team 2', 'Team 1 Odds', 'Team 2 Odds'], data=arr)
