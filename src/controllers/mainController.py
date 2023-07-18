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

                for i in range(TournamenController.tournaments[-1].number_rounds):
                    new_round = RoundController.create_round()
                    TournamenController.tournaments[-1].add_round(new_round)
                    matche = new_round.get_match_pairing(
                        RoundController.round_players, len(TournamenController.tournaments[-1].rounds))
                    print('Match created: ', matche)

                    for j in range(TournamenController.tournaments[-1].number_rounds):
                        score1, score2, player1, player2 = matche[j]
                        MatcheController.create_match(new_round, score1, score2, player1, player2)

                    for m in range(0, len(new_round.matches)):
                        MatcheController.resume_match(new_round.matches[m])
                    RoundController.resume_round(new_round)

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
