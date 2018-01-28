import json
import requests
import math
import os

from flask import Flask, jsonify


app = Flask(__name__, static_url_path='')


@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/api/summary")
def summary():
    # 1st Half
    url = "http://conu.astuce.media/api/sports/football/events.json?event=181b6efc9d744b99a905a80f013d0fc9&LevelOfDetail=high"
    response = requests.get(url)
    root = json.loads(response.content)
    goals = []
    homeTeam = root["Results"][0]["TeamHomeSummary"]
    for goal in homeTeam["Goals"]:
        goals.append(goal["TimeElapsed"])
    visitorTeam = root["Results"][0]["TeamVisitorSummary"]
    for goal in visitorTeam["Goals"]:
        goals.append(goal["TimeElapsed"])
    rv = {
        "goals": goals
    }
    return jsonify(rv)

@app.route("/api/video/<time>")
def tate_is_garbage(time):
    r = requests.get('http://conu.astuce.media/api/sports/football/events.json?event=181b6efc9d744b99a905a80f013d0fc9&LevelOfDetail=high')
    data = json.loads(r.text)



    AffiliationId =   data['Results'][0]['AffiliationId']
    EventCode = data['Results'][0]['Code']

    Team_url = 'http://conu.astuce.media/api/sports/football/team/formation.json?Affiliation='+ AffiliationId+ '&Event=' + EventCode

    t = requests.get(Team_url)
    data_t = json.loads(t.text)


    # time = '00:41:02'

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

    #print(data_j)


    aaaa = requests.get('http://conu.astuce.media:9993/api/sports/football/person/stats?Coverage=Season&Take=22&Skip=0&affiliation=17435833f1ed42848320a80f013bbb3f&season=84f210d08e644c6e89e4a80f013cf46b&OrderBy=-Goals&format=json')
    aaaa = json.loads(aaaa.text)
    for data in aaaa['Results']:

        if data['Code']  == Code:
            data['Statistics']['Goal Precentage']  = str((data['Statistics']['Goals'] * 100 ) / math.ceil(data['Statistics']['ShotsTotal']))  + "%"
            data['Statistics']['On Target Precentage']  = str((data['Statistics']['ShotsOnTarget'] * 100 ) / math.ceil(data['Statistics']['ShotsTotal']))  + "%"
            return_file = {
                "Name" : data["Name"],
                "Goal" : data['Statistics']['Goals'],
                "Shots" : data['Statistics']['ShotsTotal'],
                "ShotsOnTarget" : data['Statistics']['ShotsOnTarget'],
                "Goal Precentage " : data['Statistics']['Goal Precentage'],
                "On Target Precentage" : data['Statistics']['On Target Precentage']
            }
            print("Name: "  + (data["Name"]))
            print("Goal : " + str(data['Statistics']['Goals'] ))
            print("Shots : " + str(data['Statistics']['ShotsTotal']))
            print("ShotsOnTarget: " + str(data['Statistics']['ShotsOnTarget']))
            print("Goal Precentage " +  data['Statistics']['Goal Precentage'])
            print("On Target Precentage " +  data['Statistics']['On Target Precentage'])

    # print(return_file)
    return jsonify(return_file)

@app.route('/api/videos')
def get_videos():
    names = os.listdir(os.path.join(app.static_folder, 'videos'))
    files = []
    for name in names:
        files.append(name)
    files.sort()
    rv = {
        "files": files
    }
    return jsonify(rv)

