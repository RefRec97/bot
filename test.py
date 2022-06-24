import urllib.request, json
import player
import db

def create_player(json_player):
    playerId = json_player["playerId"]
    playerName = json_player["playerName"]
    playerGalaxy = json_player["playerGalaxy"]
    allianceId = json_player["allianceId"]
    allianceName = json_player["allianceName"]
    rank = json_player["rank"]
    score = json_player["score"]
    researchRank = json_player["researchRank"]
    researchScore = json_player["researchScore"]
    buildingRank = json_player["buildingRank"]
    buildingScore = json_player["buildingScore"]
    defensiveRank = json_player["defensiveRank"]
    defensiveScore = json_player["defensiveScore"]
    fleetRank = json_player["fleetRank"]
    fleetScore = json_player["fleetScore"]
    battlesWon = json_player["battlesWon"]
    battlesLost = json_player["battlesLost"]
    battlesDraw = json_player["battlesDraw"]
    debrisMetal = json_player["debrisMetal"]
    debrisCrystal = json_player["debrisCrystal"]
    unitsDestroyed = json_player["unitsDestroyed"]
    unitsLost = json_player["unitsLost"]
    data = player.make_player(playerId, playerName, playerGalaxy, allianceId, allianceName, rank, score, 
        researchRank, researchScore, buildingRank, buildingScore, defensiveRank, defensiveScore,
        fleetRank, fleetScore, battlesWon, battlesLost, battlesDraw, debrisMetal, debrisCrystal,
        unitsDestroyed, unitsLost)
    return data


with urllib.request.urlopen("https://pr0game.com/stats.json") as url:
    parsed_json = json.loads(url.read().decode())
    for json_player in parsed_json:
        data = create_player(json_player)
        db.db_send(data)
        #print(data.allianceName)
