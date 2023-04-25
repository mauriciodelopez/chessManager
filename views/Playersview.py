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
    player_list = [] 
    #fixer le nombre de tours à 4 donc 8 joueurs 
    def showMenu(self):
        print("""1 - crear un torneo (ir a la pantalla 2)
            2 - reanudar un torneo (ir a la pantalla 3)
            3 - ver informes (pantalla gi 4)
            4 - salir (cerrar)
            5 - crear jugadores""")
        input_menu = input("enter option")
        
        if input_menu == 1 : 
            self.tournament_view()#pour appeler une fonction qui se trouve dans la même classe 
            
        elif input_menu == 2 : 
        elif input_menu == 3 :
        elif input_menu == 4 :
        elif input_menu == 5 : 
            self.createPlayer
        else : print("Ingrese un valor valido")
    
    def tournament_view(self):
        inputTournament = input("enter the name of tournament")
        input_location = input("Enter the town of tournament")
        input_date_start = input("Enter the date of tournament start")
        input_date_end = input("Enter the tournament end date")
        input_rounds = input("enter the number of rounds")
        input_players = input("enter the name of palyers")
        input_time_control = input("enter the time_control")
        input_description = input("enter description of tournament")
        
        
        tournament = Tournament(inputTournament,input_location,input_date_start,input_date_end,input_rounds,input_players,input_time_control,input_description)
        
    def createPlayer(self):
        input_first_name = input("enter the first name")
        input_last_name = input("enter the last name")
        input_birth_date = input("enter the birth date")
        input_gender = input("enter gender")
        input_ranking = input("enter ranking")
    
        
        player = Player(input_first_name,input_last_name,input_birth_date,input_gender,input_ranking)

        self.player_list.append(player)
    
    def create_rounds(self):
        
           
    
        
       
    
    
    
        
    
    

