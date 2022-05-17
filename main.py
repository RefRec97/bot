from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import json
import player
import db
from urllib.request import urlopen
options = webdriver.ChromeOptions()
options.binary_location = "/opt/google/chrome/google-chrome"
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--headless')
options.add_argument("user-data-dir=~/.config/google-chrome")
chrome_driver_binary = "/mnt/d/Coding/graalvm-ce-java11-21.2.0/chromedriver"
browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
url = 'https://pr0game.com/stats.json'
browser.get(url)

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
  
# Give source code to BeautifulSoup
result = browser.page_source
#print(browser.page_source)
soup = BeautifulSoup(browser.page_source, 'lxml')
pre = soup.find('pre').contents[0]

#print(pre)

parsed_json = (json.loads(pre))
for json_player in parsed_json:
    data = create_player(json_player)
    db.db_send(data)


