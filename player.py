import requests
import json
r = requests.get('http://conu.astuce.media/api/sports/football/events.json?event=181b6efc9d744b99a905a80f013d0fc9&LevelOfDetail=high')
data = json.loads(r.text)
AffiliationId =   data['Results'][0]['AffiliationId']
EventCode = data['Results'][0]['Code']

Team_url = 'http://conu.astuce.media/api/sports/football/team/formation.json?Affiliation='+ AffiliationId+ '&Event=' + EventCode

t = requests.get(Team_url)
data_t = json.loads(t.text)


time = '00:03:59'

Shots = data['Results'][0]['FootballPlays']

for shit in Shots:
    if shit['TimeElapsed'] == time:
        PlayTypeCode = shit['PlayTypeCode']
        PersonId = shit['PersonId']


team_1 = data_t[0]['Layout']
team_2 = data_t[1]['Layout']

for player in team_1:
    if player['Person']['Id'] == PersonId:
     Code = player['Person']['Code']
for player in team_2:
    if player['Person']['Id'] == PersonId:
     Code = player['Person']['Code']


player_url = 'http://conu.astuce.media:9993/api/sports/football/person/stats?Affiliation=' + AffiliationId + '&Coverage=Season&&Person=' + Code
j = requests.get(player_url)
data_j = json.loads(j.text)

print(data_j)


aaaa = requests.get('http://conu.astuce.media:9993/api/sports/football/person/stats?Coverage=Season&Take=22&Skip=0&affiliation=17435833f1ed42848320a80f013bbb3f&season=84f210d08e644c6e89e4a80f013cf46b&OrderBy=-Goals&format=json')
aaaa = json.loads(aaaa.text)
for crap in aaaa['Results']:

    if crap['Code']  == Code:
        print("NIGGA?")
print(Code)
