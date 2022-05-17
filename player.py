class Player(object):
    playerId = 0
    playerName = ""
    playerGalaxy = 0
    allianceId = 0
    allianceName = ""
    rank = 0
    score = 0
    researchRank = 0
    researchScore = 0
    buildingRank = 0
    buildingScore = 0
    defensiveRank = 0
    defensiveScore = 0
    fleetRank = 0
    fleetScore = 0
    battlesWon = 0
    battlesLost = 0
    battlesDraw = 0
    debrisMetal = 0
    debrisCrystal = 0
    unitsDestroyed = 0
    unitsLost = 0

    # The class "constructor" - It's actually an initializer 
    def __init__(self, playerId, playerName, playerGalaxy, allianceId, allianceName, rank, score, 
    researchRank, researchScore, buildingRank, buildingScore, defensiveRank, defensiveScore,
    fleetRank, fleetScore, battlesWon, battlesLost, battlesDraw, debrisMetal, debrisCrystal,
    unitsDestroyed, unitsLost):
        self.playerId = playerId
        self.playerName = playerName
        self.playerGalaxy = playerGalaxy
        self.allianceId = allianceId
        self.allianceName = allianceName
        self.rank = rank
        self.score = score
        self.researchRank = researchRank
        self.researchScore = researchScore
        self.buildingRank = buildingRank
        self.buildingScore = buildingScore
        self.defensiveRank = defensiveRank
        self.defensiveScore = defensiveScore
        self.fleetRank = fleetRank
        self.fleetScore = fleetScore
        self.battlesWon = battlesWon
        self.battlesLost = battlesLost
        self.battlesDraw = battlesDraw
        self.debrisMetal = debrisMetal
        self.debrisCrystal = debrisCrystal
        self.unitsDestroyed = unitsDestroyed
        self.unitsLost = unitsLost

def make_player(playerId, playerName, playerGalaxy, allianceId, allianceName, rank, score, 
        researchRank, researchScore, buildingRank, buildingScore, defensiveRank, defensiveScore,
        fleetRank, fleetScore, battlesWon, battlesLost, battlesDraw, debrisMetal, debrisCrystal,
        unitsDestroyed, unitsLost):

    player = Player(playerId, playerName, playerGalaxy, allianceId, allianceName, rank, score, 
        researchRank, researchScore, buildingRank, buildingScore, defensiveRank, defensiveScore,
        fleetRank, fleetScore, battlesWon, battlesLost, battlesDraw, debrisMetal, debrisCrystal,
        unitsDestroyed, unitsLost)
        
    return player