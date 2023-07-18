from views.MainView import MainView
from controllers.tournamentController import TournamenController
from controllers.playerController import PlayerController
from controllers.roundController import RoundController
from controllers.matcheController import MatcheController
from views.playerView import PlayerView


class MainController:
    selected = []

    @classmethod
    def main_menu(cls):
        choice = None
        while (choice != 0):
            choice = MainView.showMenu()
            # creation of new tournament
            if choice == 1:
                TournamenController.create_tournament()

            # create player
            elif choice == 2:
                PlayerController.createPlayer()

            # add player of the tournament from default db
            elif choice == 3:
                PlayerController.showplayer()
                print("\nPlease, insert  8 players: ")

                while len(TournamenController.tournaments[-1].players) < 8:

                    id = PlayerView.get_player()
                    if id in cls.selected:
                        print("the id of player is repeated")
                    else:
                        cls.selected.append(id)
                        TournamenController.tournaments[-1].add_player(PlayerController.players[id])
                        (RoundController.round_players) =\
                            {player.ID: 0 for player in TournamenController.tournaments[-1].players}
                
                RoundController.generate_matches(TournamenController.tournaments[-1])
                TournamenController.get_winner()
                cls.selected = []
                
                # resume_data = MainView.resume_tournament_view
                # print('Final score', resume_data)

                TournamenController.get_winner()
                cls.selected = []

            elif choice == 4:
                TournamenController.show_tournament()
                PlayerController.showplayer()
                TournamenController.get_winner()

            elif choice == 5:
                MainView.generateJson(TournamenController.tournaments, TournamenController.winners)
                print("file generated")

            elif choice == 0:
                print("Exit...")
