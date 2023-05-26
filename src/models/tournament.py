class Tournament():
    
    tournament_list = []

    def __init__(self, name, location, date_start, date_end, rounds, time_control, description):
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.rounds = rounds
        self.players = []
        self.time_control = time_control
        self.description = description
        
    def add_player(self,player):
        self.players.append(player)
        
    def return_players(self):
        return self.players
        
        
   
        
     