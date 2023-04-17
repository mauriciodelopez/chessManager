#from {archivo} import {clase}

from models.players import Player
from models.round import Round
from models.tournament import Tournament

#definir la clase, para empezar a crear la vista, la vista es un objeto, y tiene atributos 

#separar tareas, dividir las responsabilidades 
#menu(metodo) submenu(submetodo un metodo que llama otro metodo)

class Playersview:
    def __init__(self, playercontroller):
        self.playercontroller = playercontroller
        
    #definir metodos de la vista las acciones que debe hacer la vista 
    
    #menu : crear jugador pedir la informacion para crear el objeto a travez de la instancia
    #first_name, last_name, birth_date, gender, ranking
    
    def get_first_name (self):
        inputfirst_name = input("Enter player name")
        player = Player(inputfirst_name) # este objeto estara stock en la variable player 
        
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
        player_ranking = input(input_ranking)    
        
    
    #creo todas las vistas en un solo archivo, por tema de simplicidad y claridad 
    #aqui estoy creando round name, round_number,matches_list=[], start_time="",end_time=    
    def get_round_name (self):
        input_round_name = input("ecrire le nombre du round")
        nameRound = Round(input_round_name)
    
    def get_round_number(self):
        input_round_number = input("ecrire le numéro de round")
        round_number = Round(input_round_number)
        
    def get_matches_list(self):
        input_matches_list = input("list de mathches")
        round_matchesList = Round(input_matches_list)
    
    def get_start_time(self):
        input_start_time = input("temps de départ")
        round_startTime = Round(input_start_time)    
    
    def get_end_time(self):
        input_end_time = input("temps de fin ")
        round_endTime = Round(input_end_time)    
        
       
    #metodo para tournament  name, location, date_start, date_end, rounds, players, time_control, description
    def createtournament (self):
        inputTournament = input("ingrese el nombre del torneo")
        nameTournament = Tournament(inputTournament)
    
    def get_location(self):
        input_location = input("ecrire la ville du tournoi")
        toournament_Location = Tournament(input_location)
    
    def get_date_start(self):
        input_date_start = input("ecrire la date du debut du tournoi")
        toournament_date_start = Tournament(input_date_start)
        
    def get_date_end(self):
        input_date_end = input("ecrire la date de fin du tournoi")
        toournament_date_end = Tournament(input_date_end)
        
    def get_rounds(self):
        input_rounds = input("ecrire le nobmre de rounds")
        toournament_rounds = Tournament(input_rounds)
        
    def get_players(self):
        input_players = input("ecrire les jouers")
        toournament_players = Tournament(input_players)
        
    def get_time_control(self):
        input_time_control = input("ecrire le time_control")
        toournament_time_control = Tournament(input_time_control)
        
    def get_description(self):
        input_description = input("ecrire la description du tournoi")
        toournament_description = Tournament(input_description)                        
        
        
    
    

