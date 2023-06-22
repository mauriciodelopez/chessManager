class Tournament():
    
    

    def __init__(self, ID, name, location, date_start, date_end, description):
        self.ID =ID
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.number_rounds = 4
        self.rounds = []
        self.players = []
        self.description = description
        
    def __str__(self):
        player_str = "\n\n".join(str(player) for player in self.players)
        round_str = "\n\n".join(str(round) for round in self.rounds)
        
        return  f" DETAILS OF TOURNAMENT:\n\nID = {self.ID}, " \
                    f"name =  {self.name}, " \
                    f"location = {self.date_start}, " \
                    f"date_start = {self.date_start}, " \
                    f"date_end = {self.date_end}, " \
                    f"\n\nROUNDS OF TOURNAMENT:\n rounds = {round_str}, " \
                    f"\n\nPLAYERS OF TOURNAMENT:\nplayers = {player_str}, " \
                    f"description = {self.description}, "
                    
                
        
    def add_player(self,player):    
        self.players.append(player)
    
    def add_round(self,round):
        self.rounds.append(round)
               
    def return_players(self):
        return self.players
    
        
        
   
        
     