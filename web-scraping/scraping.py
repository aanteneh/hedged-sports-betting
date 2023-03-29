# Scraping Method general file

import pandas as pd
from re import match

# for some reason have to follow this request convention
hdr = {'User-Agent': 'Mozilla/5.0'}


def only_numerics(seq):
    seq_type = type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))


def convert_units(odd):
    res = []
    for i in range(len(odd)):
        print(only_numerics(odd[i]))

        # if match(r'^-?[0-9]+$', odd[i]):
        #     if (int(float(odd[i])) >= 0):
        #         res.append(int(float(odd[i]))/100+1)
        #     else:
        #         res.append(1-(100/int(float(odd[i]))))
        # else:
        #     print("failed check")
    return res


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
    for i in range(0, len(teams), 2):
        r = []
        r.append(teams[i])
        r.append(teams[i+1])
        r.append(odds[i])
        r.append(odds[i+1])
        arr.append(r)
    return pd.DataFrame(columns=['Team 1', 'Team 2', 'Team 1 Odds', 'Team 2 Odds'], data=arr)
