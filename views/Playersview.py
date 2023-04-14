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
    
    def get_last_name (self):
        inputfirst_name = input("Enter player name")
        player = Player(inputfirst_name) # este objeto estara stock en la variable player 
        
    def get_last_name(self):
        inputlast_name = input("Enter player last name")
        player_lastname = Player(inputlast_name)
        
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
    def createround (self):
        inputRound = input("ingrese el nombre del round")
        nameRound = Round(inputRound)
        
    
        
    #metodo para tournament  name, location, date_start, date_end, rounds, players, time_control, description
    def createtournament (self):
        inputTournament = input("ingrese el nombre del torneo")
        nameTournament = Tournament(inputTournament)
        
    
    

