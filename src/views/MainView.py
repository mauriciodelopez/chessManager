#from {archivo} import {clase}

#from controllers.TournamentController import TournamentController
from models.tournament import Tournament
#tc = TournamentController()

class MainView:
    
    @classmethod   
    def showMenu(cls):
        print('Hello, please select a action')
        print('1: Create a tournament go view #2')
        print('2: Resume tournament go view #8')
        print('3: Create players go view #5' )
        print('4: Reports go view #7')
        print('0: Exit')
        
        
    
        
        choice= -1
        while(choice < 0 or choice > 4):
            choice = int(input("enter option: "))
        
        return choice

            
    
    
    @staticmethod     
    def tournament_view():
        inputTournament = input("enter the name of tournament")
        input_location = input("Enter the town of tournament")
        input_date_start = input("Enter the date of tournament start")
        input_date_end = input("Enter the tournament end date")
        input_rounds = input("enter the number of rounds")
        #input_players = input("enter the name of palyers")
        input_time_control = input("enter the time_control")
        input_description = input("enter description of tournament")
        
        """TournamentController.create_tournament
        (
            inputTournament,
            input_location, 
            input_date_start, 
            input_date_end, 
            input_rounds, 
            input_time_control, 
            input_description
        )"""
    
        return {
            'name': inputTournament, 
            'location': input_location, 
            'date_start': input_date_start, 
            'date_end': input_date_end,
            'rounds': input_rounds, 
            #'players': input_players, 
            'time_control': input_time_control, 
            'description': input_description
            }
        
        
    @staticmethod
    def resume_tournament_view():
        input_score = input("Please enter the score of the completed match ")
        
        return{'final_score': input_score}   
    
    @classmethod
    def newplayer_view(cls):
        input_first_name = input("Insert first_name: ")
        input_last_name = input("Insert the last name of player:  ")
        input_date_of_birth = input("Insert the date_of_birth: ")
        input_gender = input("insert gender of player: ")
        
        #TournamentController.add_new_player(input_first_name, input_last_name, input_date_of_birth, input_gender)
        #cls.showplayerslist()
        #return{'first_name': input_first_name, 'last_name': input_last_name, 'date_of_birth': input_date_of_birth, 'gender': input_gender}
    
    
    """@staticmethod    
    def showplayerslist():
        players_list = TournamentController.get_players()
        for p in players_list:
            print(p.first_name)"""
    
    
    
    @staticmethod    
    def show_tournament_list(tournament_list):
        #tournament_list = TournamentController.tournaments()
        for t in tournament_list:
            print(t.name)
        
            
    

