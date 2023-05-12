#from {archivo} import {clase}

from models.players import Player
from models.round import Round
from models.tournament import Tournament
from controllers.TournamentController import TournamentController

#define the class, to create view, the view is an objet and has attributes,

#separate tasks, divide the responsabilities 
#menu(method) submenu(submetodo an methode who call an other methode)

class Playersview:
    
    tc = TournamentController()
    def showMenu(self):
        print("1-Create a tournament go view #2")
        print("2-Resume tournament go view #8")
        print("3-Create players go view #5" )
        print("4-Reports go view #7")

        input_menu = input("enter option")
        
        if input_menu == 1 : 
            self.tournament_view()#pour appeler une fonction qui se trouve dans la même classe 
            
        elif input_menu == 2 : 
        elif input_menu == 3 :
        elif input_menu == 4 :
        else : print("enter a valid value")
    
    def tournament_view(self):
        inputTournament = input("enter the name of tournament")
        input_location = input("Enter the town of tournament")
        input_date_start = input("Enter the date of tournament start")
        input_date_end = input("Enter the tournament end date")
        input_rounds = input("enter the number of rounds")
        input_players = input("enter the name of palyers")
        input_time_control = input("enter the time_control")
        input_description = input("enter description of tournament")
        
        #paso los parametros 
        self.tc.create_a_tournament(inputTournament,input_location,input_date_start,input_date_end,input_rounds,input_players,input_time_control,input_description)
        

        
           
    
        
       
    
    
    
        
    
    

