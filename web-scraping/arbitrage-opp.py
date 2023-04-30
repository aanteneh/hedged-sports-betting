import draftkings as dk
import agbets as ag

data = [dk.dkDf, ag.agDf]


def arb_game(l, game):
    res = ""
    team1max = (float('-inf'), -1)
    team2max = (float('-inf'), -1)

    # for i in range(len(l)):
    #     print(int(l[i].iloc[game][2]))

    for i in range(len(l)):
        if l[i].iloc[game][2] > team1max[0]:
            team1max = (l[i].iloc[game][2], i)
        if l[i].iloc[game][3] > team2max[0]:
            team2max = (l[i].iloc[game][3], i)
    arbit = 100*(1/team1max[0]+1/team2max[0])
    res = res + 'The best possible arbitrage % for ' + \
        l[i].iloc[game][0] + ' vs ' + \
        l[i].iloc[game][1]+' is ' + str(arbit) + '%\n'
    if arbit < 100:
        res = res + 'There is an arbitrage opportunity by betting on ' + l[i].iloc[game][0] + ' on site ' + str(
            team1max[1]) + ' and ' + l[i].iloc[game][0] + ' on site ' + str(team2max[1]) + '\n'
    elif arbit >= 0:
        res = res + 'There is no arbitrage opportunity for ' + \
            l[i].iloc[game][0] + ' vs ' + l[i].iloc[game][1]
    return res


def arb(l):
    res = []
    if not l:
        return
    num = len(l[0])
    for i in range(num):
        res.append(arb_game(l, i))
    return res


for s in arb(data):
    print(s)
