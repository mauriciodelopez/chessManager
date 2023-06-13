from views.MainView import MainView
from models.tournament import Tournament
from controllers.TournamentController import TournamentController
from models.players import Player
from models.round   import Round
from models.matches import Matche



class MainController:
 
    tournaments = []
    players = []
    
    @classmethod
    def main_menu(cls):
        choice = None
        while (choice != 0):
            choice = MainView.showMenu()
        
            if choice == 1 :
                tournament_data = MainView.tournament_view()
                new_tournament = Tournament(
                    len(cls.tournaments) + 1,
                    tournament_data['name'],
                    tournament_data['location'],
                    tournament_data['date_start'],
                    tournament_data['date_end'],
                    #tournament_data['number_rounds'],
                    tournament_data['time_control'],
                    tournament_data['description'])
    
                
                cls.tournaments.append(new_tournament)
                #MainView.show_tournament_list(TournamentController.tournaments)
                    
            elif choice == 2 :
                
                resume_data = MainView.resume_tournament_view()
                print('final score', resume_data)
                
                
                
            elif choice == 3 :
                      
                player_data = MainView.newplayer_view()
                new_player = Player(
                    len(cls.players) + 1,
                    player_data['first_name'],
                    player_data['last_name'],
                    player_data['date_of_birth'],
                    player_data['gender']
                    )
                
                cls.players.append(new_player)
                
                new_tournament.add_player(new_player)
                
            elif choice == 4 :
                round_data = MainView.round_view()
                new_round = Round(
                    round_data['name'],
                    round_data['round_number'],
                    round_data['start_time'],
                    round_data['end_time'],
                        )
                new_tournament.add_round(new_round)
                
            elif choice == 5 :
                match_data = MainView.match_view()
                new_match = Matche(
                    match_data['scorePlayer1'],
                    match_data['scorePlayer2'],
                    match_data['player1'],
                    match_data['player2'],
                        )
                new_round.add_matche(new_match) 
                
            
                       
            elif choice == 6 :
                
                
                print("\n-----Tournaments----\n")
                
                MainView.show_tournament_list(cls.tournaments)
                
                print("\n-----Players----\n")

                MainView.show_players_list(cls.players)
                
                
                
            elif choice== 0 :
                print("Exit...")
           