# -*- coding: utf-8 -*-

class IPLPlayer():
    def __init__(self):    
        self.playersInTeam = {}
        self.playerListRCB = []
        self.playerListCSK = []
        
    def addPlayers(self,team,pname):
        self.team = team
        self.pname = pname
        if (self.team == 'RCB'):
            self.playerListRCB.append(self.pname)
            self.playersInTeam[self.team] = self.playerListRCB
        elif (self.team == 'CSK'):
            self.playerListCSK.append(self.pname)
            self.playersInTeam[self.team] = self.playerListCSK

iplplayer = IPLPlayer()
iplplayer.addPlayers("RCB","Virat")
iplplayer.addPlayers("RCB","ABD")
iplplayer.addPlayers("CSK","Dhoni")
iplplayer.addPlayers("CSK","Raina")

print('players in the team RCB ', iplplayer.playerListRCB)
print('players in the team RCB ', iplplayer.playerListCSK)

for t,p in iplplayer.playersInTeam.items():
    print (t)
    print(p)


