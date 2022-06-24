CREATE TABLE alliances(
	allianceId int,
    name varchar(255),
    tag varchar(8),
    constraint pk_alliances primary key (allianceId)
);

Create TABLE players(
    playerId int,
    name varchar(255),
    galaxy int,
    allianceId int,
    CONSTRAINT PK_players PRIMARY KEY (playerId),
    CONSTRAINT FKplayerAlliances FOREIGN KEY (allianceId) 
    REFERENCES alliances(allianceId)
);

Create TABLE data(
	playerId int,
    generalRank int,
    generalScore int,
    fleetRank int,
    fleetScore int,
    researchRank int,
    researchScore int,
    buildingRank int,
    buildingScore int,
    defensiveRank int,
    defensiveScore int,
    battlesWon int,
    battlesLost int,
    battlesDraw int,
    debrisMetal int,
    debrisCrystal int,
    unitsDestroyed int,
    unitsLost int,
    date DATETIME,
    CONSTRAINT PK_data PRIMARY KEY (playerId,date),
    CONSTRAINT FKdataPlayer FOREIGN KEY (playerId) 
    REFERENCES players(playerId)
);

create table auth(
	authUser varchar(255),
    role varchar(255),
    CONSTRAINT PK_auth PRIMARY KEY (authUser)
);
insert into auth values ("reflexrecon#8323", "admin");

create table research(
	name varchar(255),
    level int,
    metal int,
    crytal int,
    deuterium int,
    CONSTRAINT PK_research PRIMARY KEY (name,level)
);

create table buildings(
	name varchar(255),
    level int,
    metal int,
    crystal int,
    deuterium int,
    CONSTRAINT PK_buildings PRIMARY KEY (name,level)
);

create table ships(
	name varchar(255),
    metal int,
    crystal int,
    deuterium int,
    CONSTRAINT PK_ships PRIMARY KEY (name)
);

create table planets(
	galaxy int,
    solarsystem int,
    position int,
    playerId int,
    CONSTRAINT PK_planets PRIMARY KEY (galaxy,solarsystem,position),
    CONSTRAINT FK_planetsPlayer FOREIGN KEY (playerId) 
    REFERENCES players(playerId)
);

create table moons(
	galaxy int,
	solarsystem int,
    position int,
    playerId int,
    phalanxlvl int,
    baselvl int,
    robotlvl int,
    jumpgate int,
    CONSTRAINT PK_moons PRIMARY KEY (galaxy,solarsystem,position),
    CONSTRAINT FK_moonsPlayer FOREIGN KEY (playerId) 
    REFERENCES players(playerId)
);

create table coalitions(
	allianceId int,
    partnerAllianceId int,
    wing bool DEFAULT false,
    CONSTRAINT FKcoalitionsAlliancesStart FOREIGN KEY (allianceId)
    REFERENCES alliances(allianceId),
    CONSTRAINT FKcoalitionsAlliancesTarget FOREIGN KEY (partnerAllianceId)
    REFERENCES alliances(allianceId),
    CONSTRAINT PKcoalitions PRIMARY KEY (allianceId, partnerAllianceId)
);

create table updates(
	channelId varchar(255),
    CONSTRAINT PKcoalitions PRIMARY KEY (channelId)
);