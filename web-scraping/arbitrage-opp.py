import pandas as pd
import draftkings as dk
import agbets as ag

data = [dk.dkDf, ag.agDf]


def a_game(l, game):
    res = ""
    t1_odds = []
    t2_odds = []
    t1_max = (float('-inf'), -1)
    t2_max = (float('-inf'), -1)
    for i in range(len(l)):
        if l[i].iloc[game][2] > t1_max[0]:
            t1_max = (l[i].iloc[game][2], i)
        if l[i].iloc[game][3] > t2_max[0]:
            t2_max = (l[i].iloc[game][3], i)

    return res
