import json
import requests

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def home():
    return "Daddy's home"


@app.route("/summary")
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
