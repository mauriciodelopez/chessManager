#from views.Playersview import Playersview
from models.tournament import Tournament
from models.matches import Matche
from models.players import Player

class TournamentController:
    tournament = None
    #def __init__(self):
        #self.pv = Playersview()
    
    """def showMenu(self):
        choice = self.pv.showMenu()
        if choice == "1":
            self.tournament_view()
        elif choice == "2":
            self.resume_tournament_view()
        elif choice == "3":
            self.newplayer_view()"""
    
        
    def tournament_view(self):
        tournament_values = self.pv.tournament_view()
        nouveautournois = Tournament(tournament_values['name'], tournament_values['location'], tournament_values['date_start'], tournament_values['date_end'], tournament_values['rounds'], tournament_values['players'], tournament_values['time_control'], tournament_values['description'])
        
        print(nouveautournois.name)
        print(nouveautournois.location)
        print(nouveautournois.date_start)
        print(nouveautournois.date_end)
        print(nouveautournois.rounds)
        print(nouveautournois.players)
        print(nouveautournois.time_control)
        print(nouveautournois.description)
        
    def create_tournament(self, inputTournament, input_location, input_date_start, input_date_end,
                          input_rounds, input_time_control, input_description):
        self.tournament = Tournament(inputTournament, input_location, input_date_start, input_date_end, 
                                     input_rounds, input_time_control, input_description)
        
        
    def resume_tournament_view(self):
        resume_values = self.pv.resume_tournament_view()
        nouveauresume = Matche(resume_values['final_score'])
        
        print(nouveauresume.final_score)
        
    def add_new_player(self, input_first_name, input_last_name, input_date_of_birth, input_gender):
        player = Player(input_first_name, input_last_name, input_date_of_birth, input_gender)
        self.tournament.add_player(player)
        
        
    def get_players(self):
        return self.tournament.return_players()
        
        
        
        
        
              
        