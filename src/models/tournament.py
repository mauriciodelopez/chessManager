class Tournament():
    
    

    def __init__(self, ID, name, location, date_start, date_end, time_control, description):
        self.ID =ID
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.number_rounds = 4
        self.rounds = []
        self.players = []
        self.time_control = time_control
        self.description = description
        
    def __str__(self):
        return f"name =  {self.name},location = {self.date_start}, date_start = {self.date_start}, date_end = {self.date_end}, time_control = {self.time_control}, description = {self.description}"
        
    def add_player(self,player):    
        self.players.append(player)
    
    def add_round(self,round):
        self.rounds.append(round)
               
    def return_players(self):
        return self.players
    
        
        
   
        
     