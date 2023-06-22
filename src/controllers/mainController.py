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
                    tournament_data['description'])
    
                
                cls.tournaments.append(new_tournament)
                #MainView.show_tournament_list(TournamentController.tournaments)
                    
            elif choice == 2 :
                resume_data = MainView.resume_tournament_view
                print('Final score', resume_data)
                
                
                
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
                
                
                
            elif choice == 4 :
                print("Players: ",MainView.show_players_list(cls.players))
                num_players=int(input("\nInsert the number of players: "))
                for i in range (num_players):
                    id = MainView.get_player()
                    new_tournament.add_player(cls.players[id])

                
            elif choice == 5 :
                round_data = MainView.round_view()
                new_round = Round(
                    round_data['name'],
                    round_data['round_number'],
                    start_time = ["start_time"]
                                )
                new_tournament.add_round(new_round)
                
            elif choice == 6 :
                matche = new_round.get_match_pairing(new_tournament.players)
                print('test', matche)
                new_match=Matche(*matche)#nous ecrivons l'étoile afin de pouvoir unpacking of the tuple
                new_round.add_matche(new_match) 
                
            elif choice == 7 :
                
                score_player1, score_player2, index = MainView.resume_match_view()
                for i in range(0, len(new_round.matches)):
                    
                    if i == index : 
                
                        new_round.matches[i].scorePlayer1 += score_player1 #+= for cumulate in order additioned to the last result
                        new_round.matches[i].scorePlayer2 += score_player2
                
                
                
            elif choice == 8 :             
                print("\n-----Tournaments----\n")
                
                MainView.show_tournament_list(cls.tournaments)
                
                print("\n-----Players----\n")

                MainView.show_players_list(new_tournament.players)




                
            elif choice == 9 :
                new_tournament = Tournament(len(cls.tournaments) + 1,'Ta','Paris','12/07/2023','12/07/2023', 'Director')
                cls.tournaments.append(new_tournament)
                new_player1 = Player(len(cls.players) + 1,'carlie1','dupond1','12/07/1989','male')
                cls.players.append(new_player1)
                new_player2 = Player(len(cls.players) + 1,'charlie2','dupond2','12/07/1989','male')
                cls.players.append(new_player2)
                new_player3 = Player(len(cls.players) + 1,'charlie3','dupond3','12/07/1989','male')
                cls.players.append(new_player3)
                new_player4 = Player(len(cls.players) + 1,'carlie4','dupond4','12/07/1989','male')
                cls.players.append(new_player4)
                new_player5 = Player(len(cls.players) + 1,'charlie5','dupond5','12/07/1989','male')
                cls.players.append(new_player5)
                new_player6 = Player(len(cls.players) + 1,'charlie6','dupond6','12/07/1989','male')
                cls.players.append(new_player6)
                print("created")
               
                
            elif choice== 0 :
                print("Exit...")
           