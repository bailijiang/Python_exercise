__author__ = 'Bryan'

basketball_players = {
    'yaoming': {
        'first': 'yao',
        'last': 'ming',
        'team': 'rocket',
    },
    'kobebryant': {
        'first': 'kobe',
        'last': 'bryant',
        'team': 'laker',
    },
    'stevencurry': {
        'first': 'steven',
        'last': 'curry',
        'team': 'warrior'
    },
}

for playername, player_info in basketball_players.items():
    print("PlayerName: " + playername)
    full_name = player_info['first'] + " " + player_info['last']
    team = player_info['team']

    print("\tFull name: " + full_name)
    print("\tteam: " + team)