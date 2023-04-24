# Scraping Method general file

import pandas as pd
from re import match

# for some reason have to follow this request convention
hdr = {'User-Agent': 'Mozilla/5.0'}

abbrev_names = {'AtlantaHawks': 'ATL', 'ATLHawks': 'ATL', 'BostonCeltics': 'BOS', 'BOSCeltics': 'BOS',
                'BrooklynNets': 'BKN', 'BKNNets': 'BKN', 'CharlotteHornets': 'CHA', 'CHAHornets': 'CHA',
                'ChicagoBulls': 'CHI', 'CHIBulls': 'CHI', 'ClevelandCavaliers': 'CLE', 'CLECavaliers': 'CLE', 'DallasMavericks': 'DAL', 'DALMavericks': 'DAL',
                'DenverNuggets': 'DEN', 'DENNuggets': 'DEN', 'DetroitPistons': 'DET', 'DETPistons': 'DET',
                'GoldenStateWarriors': 'GSW', 'GSWWarriors': 'GSW', 'GSWarriors': 'GSW', 'HoustonRockets': 'HOU', 'HOURockets': 'HOU',
                'IndianaPacers': 'IND', 'INDPacers': 'IND', 'LosAngelesClippers': 'LAC', 'LAClippers': 'LAC',
                'LosAngelesLakers': 'LAL', 'LALakers': 'LAL', 'MemphisGrizzlies': 'MEM', 'MEMGrizzlies': 'MEM',
                'MiamiHeat': 'MIA', 'MIAHeat': 'MIA', 'MilwaukeeBucks': 'MIL', 'MILBucks': 'MIL',
                'MinnesotaTimberwolves': 'MIN', 'MINTimberwolves': 'MIN', 'NewOrleansPelicans': 'NOP',
                'NOPelicans': 'NOP', 'NewYorkKnicks': 'NYK', 'NYKnicks': 'NYK', 'OklahomaCityThunder': 'OKC',
                'OKCThunder': 'OKC', 'OrlandoMagic': 'ORL', 'ORLMagic': 'ORL', 'Philadelphia76ers': 'PHI',
                'PHI76ers': 'PHI', 'PhoenixSuns': 'PHX', 'PHXSuns': 'PHX', 'PHOSuns': 'PHX', 'PortlandTrailBlazers': 'POR',
                'PORTrailBlazers': 'POR', 'SacramentoKings': 'SAC', 'SACKings': 'SAC', 'SanAntonioSpurs': 'SAS',
                'SASpurs': 'SAS', 'TorontoRaptors': 'TOR', 'TORRaptors': 'TOR', 'UtahJazz': 'UTA', 'UTJazz': 'UTA',
                'WashingtonWizards': 'WAS', 'WASWizards': 'WAS'}


def only_numerics(seq):
    seq_type = type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))


def convert_units(odd):
    res = []
    for k in range(len(odd)):
        if (int(odd[k]) >= 0):
            res.append(float(odd[k])/100+1)
        else:
            res.append(1-(100/float(odd[k])))
    return res


def get_names(content):
    arr = []
    for c in content:
        arr.append(abbrev_names[c.getText().replace(
            '\n', '').replace('\t', '').replace(' ', '')])
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
