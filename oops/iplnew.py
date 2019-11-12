class Player():
    def __init__(self, season,name, team, matches,runs,wickets=None):
        self.season = season
        self.name = name
        self.team = team
        self.matches = matches
        self.runs = runs
        self.wickets = wickets

class IPL ():
    def __init__(self):
        self.iplplayes = []
        self.maxruns = []
        self.maxwickets = []      

    def add(self, player):
        player_dictionary = {
            'season': player.season,
            'name': player.name,
            'matches': player.matches,
            'runs': player.runs,
            'wickets': player.wickets,
            
            }
        self.iplplayes.append(player_dictionary)
        print (player.name, 'player appended')
            
    def maximumruns(self,season):
        for player in self.iplplayes:
            
            if player['season'] == season:
                self.maxruns.append(player['runs'])
        
        playerindex = self.maxruns.index(max(self.maxruns))
        
        
        return self.iplplayes[playerindex]
    
#season,name, team, matches,runs,wickets
ipl = IPL()
player1 = Player(2018, 'Virat', 'RCB', 15,800)
ipl.add(player1)

player2 = Player(2018, 'ABD', 'RCB', 10,750)
ipl.add(player2)

player3 = Player(2018, 'Maxwell', 'XKIP', 10,850)
ipl.add(player3)

print('ipl player ',ipl.iplplayes)
player = ipl.maximumruns(2018)
print(' Maximum run getter ' ,player)


