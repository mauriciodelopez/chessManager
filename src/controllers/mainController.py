from views.MainView import MainView
from models.tournament import Tournament
from controllers.TournamentController import TournamentController



class MainController:
 
 
    
    @staticmethod
    def main_menu():
        choice = None
        while (choice != 0):
            choice = MainView.showMenu()
        
            if choice == 1 :
                tournament_data = MainView.tournament_view()
                tournament = Tournament(
                    tournament_data['name'],
                    tournament_data['location'],
                    tournament_data['date_start'],
                    tournament_data['date_end'],
                    tournament_data['rounds'],
                    tournament_data['time_control'],
                    tournament_data['description'])
                
                TournamentController.tournaments.append(tournament)
                MainView.show_tournament_list(TournamentController.tournaments)
                    
            elif choice == 2:
                MainView.resume_tournament_view()
            elif choice == "3":
                MainView.newplayer_view()
            elif choice == "4":
                MainView.tournament_get()
            elif choice=="0":
                print("Exit...")
           