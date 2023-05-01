#!pip install sportmonks

from sportmonks.soccer import SoccerApiV2
soccer = SoccerApiV2(api_token='TYzm2GbS0IK868HeTvOOPU4uJPzsDrYl4bAbAwYxRcPHVSMo2QcezalZJsOD')


fixtures = soccer.fixtures_today(includes=('localTeam', 'visitorTeam','odds', 'flatOdds'))
for f in fixtures:
    print(f['localTeam']['name'], 'plays at home against', f['visitorTeam']['name'])
    print(f['odds'], f['flatOdds'])
