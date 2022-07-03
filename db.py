import datetime
from pickle import NONE
from readline import insert_text
from datetime import datetime
import mysql.connector
import player
import config
def db_send(player):
    # Creating connection object
    mydb = mysql.connector.connect(
        host = config.dbRemoteIP,#server
        #host="192.168.0.104",#local
        user = config.dbUsername,
        password = config.dbPassword,
        database = config.dbSchema
    )
 
    # Printing the connection object
    #print(mydb)

    select_cursor = mydb.cursor(buffered=True)
    insert_cursor = mydb.cursor()
    
    #check ally
    select_cursor.execute("select * from alliances where alliances.allianceId = "+player.allianceId)
    row_count = select_cursor.rowcount
    if row_count == 0:
        #print("new ally id, name: "+player.allianceId+", "+player.allianceName)
        insert_cursor.execute("insert into alliances (allianceId, name) values (%s, %s);", (player.allianceId, player.allianceName))
        mydb.commit()

    #check player
    select_cursor.execute("select * from players where players.playerid = "+player.playerId)

    row_count = select_cursor.rowcount
    if row_count == 0:
        #print("new player id, name, gala, allyid: "+player.playerId+", "+player.playerName+", "
        #+player.playerGalaxy+", "+player.allianceId)

        insert_cursor.execute("insert into players values (%s, %s, %s, %s);",(player.playerId, player.playerName, 
        player.playerGalaxy, player.allianceId))
        mydb.commit()
    #todo: else with overrides for playername and allianceid if they changed
    else:
        select_cursor.execute("select playerId, name, allianceId from players where players.playerid = "+player.playerId)
        playerData = select_cursor.fetchall()
        for row in playerData:
            if(row[1] != player.playerName):
                insert_cursor.execute("UPDATE players SET name= %s where playerId =%s;",(player.playerName, player.playerId))
            if(row[2] != player.allianceId):
                insert_cursor.execute("UPDATE players SET allianceId= %s where playerId =%s;",(player.allianceId, player.playerId))
        mydb.commit()
    
    insert_cursor.execute("insert into data values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
    (player.playerId, player.rank, player.score, player.fleetRank, player.fleetScore, 
    player.researchRank, player.researchScore, player.buildingRank, player.buildingScore,
    player.defensiveRank, player.defensiveScore, player.battlesWon, player.battlesLost,
    player.battlesDraw, player.debrisMetal, player.debrisCrystal, player.unitsDestroyed, 
    player.unitsLost, datetime.now()))
    mydb.commit()
    mydb.close()
    
