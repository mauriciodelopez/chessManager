#from {archivo} import {clase}

from models.players import Player
from models.round import Round
from models.tournament import Tournament

#define the class, to create view, the view is an objet and has attributes,

#separate tasks, divide the responsabilities 
#menu(method) submenu(submetodo an methode who call an other methode)

class Playersview:
    def __init__(self, playercontroller):
        self.playercontroller = playercontroller
        
    #define methodes of the view the actions that the view have to do d 
    
    #menu : create player, to ask information for to create objet througt an instance 
    #first_name, last_name, birth_date, gender, ranking
    
    def get_first_name (self):
        inputfirst_name = input("Enter player name")
        player = Player(inputfirst_name) # this objet este objeto estara stock en la variable player 
        
    def get_last_name(self):
        input_last_name = input("Enter player last name")
        player_lastname = Player(input_last_name)
        
    def get_birth_date(self):
        input_birth_date = input("enter your birth date")
        player_birth_date = Player(input_birth_date)
        
    def get_gender(self):
        input_gender = input("Enter your gender")
        player_gender = Player(input_gender)
    
    def get_ranking(self):
        input_ranking = input("Enter your ranking")
        player_ranking = Player(input_ranking)    
        
    
    #create all views in an only file, cause is simple & clear  
    #here i create round name, round_number,matches_list=[], start_time="",end_time=    
    def get_round_name (self):
        input_round_name = input("Enter the round name")
        nameRound = Round(input_round_name)
    
    def get_round_number(self):
        input_round_number = input("Enter the round number")
        round_number = Round(input_round_number)
    
    #create an attribute in the rounds that is a list that stores, the objects of type player    
    def get_matches_list(self):
        input_matches_list = input("list of matches")
        round_matchesList = Round(input_matches_list)
    
    def get_start_time(self):
        input_start_time = input("start time")
        round_startTime = Round(input_start_time)    
    
    def get_end_time(self):
        input_end_time = input("end time ")
        round_endTime = Round(input_end_time)    
        
       
    #methode for tournament  name, location, date_start, date_end, rounds, players, time_control, description
    def get_tournament_name (self):
        inputTournament = input("enter the name of tournament")
        nameTournament = Tournament(inputTournament)
    
    def get_location(self):
        input_location = input("Enter the town of tournament")
        toournament_Location = Tournament(input_location)
    
    def get_date_start(self):
        input_date_start = input("Enter the date of tournament start")
        toournament_date_start = Tournament(input_date_start)
        
    def get_date_end(self):
        input_date_end = input("Enter the tournament end date")
        toournament_date_end = Tournament(input_date_end)
        
    def get_rounds(self):
        input_rounds = input("enter the number of rounds")
        toournament_rounds = Tournament(input_rounds)
        
    def get_players(self):
        input_players = input("enter the name of palyers")
        toournament_players = Tournament(input_players)
        
    def get_time_control(self):
        input_time_control = input("enter the time_control")
        toournament_time_control = Tournament(input_time_control)
        
    def get_description(self):
        input_description = input("enter description of tournament")
        toournament_description = Tournament(input_description)                        
        
        
    
    

