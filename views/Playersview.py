#from {archivo} import {clase}

"""
Tengo que hacer lo siguiente :
PANTALLA 1
1 - crear un torneo (ir a la pantalla 2)
2 - reanudar un torneo (ir a la pantalla 3)
3 - ver informes (pantalla gi 4)
4 - salir (cerrar)
Pantalla 2
Pregunta por la fecha
pregunta por el nombre
Preguntar para elegir jugadores de la lista
Validar (ir a pantalla 7)
Pantalla 3
Pida elegir torneos de la lista (vaya a la pantalla 7)
Pantalla 4
1- ver informe ordenado por nombres (ir pantalla 5)
2- ver informe ordenado por puntaje (ir pantalla 6)
Pantalla 5
Vista del informe
Pantalla 6
Vista del informe
Pantalla 7
1- ingrese el puntaje de un partido (vaya a la pantalla 9)
2- cambiar la clasificación del jugador (ir a la pantalla 8)
3 - Terminar el torneo (ir a pantalla 1)
"""

""" modèles :

Ecrire la succecion des ecrans 
○ Avec quelles entités votre programme va-t-il fonctionner?

○ Doivent-elles contenir des données (= attributs)?

○ Possèdent-elles des comportements spécifiques (= méthodes)?

● Pour commencer, votre programme s’appuiera (au minimum) sur des
tournois, des tours, des matchs et des joueurs.

○ Quels sont les attributs requis pour chacune de ces entités?

○ Quels sont les comportements de ces entités? Par exemple,
comment les joueurs sont-ils associés lors des tours?
ex tounoi genere des tours, sous quel forme 

● L’application chargera les données du tournoi à partir d’un fichier JSON.

● Les données des joueurs seront disponibles dans le fichier JSON du
tournoi, mais vous devrez les associer avec les autres données
disponibles dans les fichiers JSON des clubs.

○ Gardez en tête l'identifiant national d’échecs (dans les
spécifications techniques).
"""

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
    
    def showMenu(self):
        print("""1 - crear un torneo (ir a la pantalla 2)
            2 - reanudar un torneo (ir a la pantalla 3)
            3 - ver informes (pantalla gi 4)
            4 - salir (cerrar)""")
        input_menu = input("enter option")
        
        if input_menu == 1 : 
            ecran2()
            
        elif input_menu == 2 : 
        elif input_menu == 3 :
        elif input_menu == 4 :
        else : print("Ingrese un valor valido")
    
    def ecran2(self):
        inputTournament = input("enter the name of tournament")
        input_location = input("Enter the town of tournament")
        input_date_start = input("Enter the date of tournament start")
        input_date_end = input("Enter the tournament end date")
        input_rounds = input("enter the number of rounds")
        input_players = input("enter the name of palyers")
        input_time_control = input("enter the time_control")
        input_description = input("enter description of tournament")
        
        
        tournament = Tournament(inputTournament,input_location,input_date_start,input_date_end,input_rounds,input_players,input_time_control,input_description)
        
        
        pantallaTorneo(tournament)
        
    def pantallaTorneo(tournament):
        
        
        
        
    
     
      
        
        
        
        
        
        
        print(""", location, date_start, date_end, rounds, players, time_control, description """)
    
    
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
        
        
    
    

