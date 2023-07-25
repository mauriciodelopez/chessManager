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
<<<<<<< HEAD
                for k in range(8):
                    id = MainView.get_player()
                    new_tournament.add_player(cls.players[id])
                    cls.round_players = {player.ID: 0 for
                                         player in new_tournament.players}

                for i in range(new_tournament.number_rounds):
                    round_data = MainView.round_view()
                    new_round = Round(
                        round_data['name'],
                        round_data['round_number'],
                        round_data['start_time']
                                    )
                    new_tournament.add_round(new_round)
                    matche = new_round.get_match_pairing(
                        cls.round_players, len(new_tournament.rounds))
                    print('Match created: ', matche)

                    for j in range(new_tournament.number_rounds):
                        score1, score2, player1, player2 = matche[j]
                        new_match = Matche(len(new_round.matches) + 1,
                                           score1, score2, player1, player2)
                        new_round.add_matche(new_match)

                    for m in range(0, len(new_round.matches)):
                        (score_player1, score_player2) =\
                         MainView.resume_match_view(
                            new_round.matches[m], new_tournament.players)
                        new_round.matches[m].scorePlayer1 += score_player1
                        new_round.matches[m].scorePlayer2 += score_player2
                        (cls.round_players[new_round.matches[m].player1]) =\
                            new_round.matches[m].scorePlayer1
                        (cls.round_players[new_round.matches[m].player2]) =\
                            new_round.matches[m].scorePlayer2

                    end_date = MainView.resume_round_view()
                    new_round.end_time = end_date

            elif choice == 4:

                print("TOURNAMENT\n")
                MainView.show_tournament_list(cls.tournaments)

                print("\nPlAYERS OF TOURNAMENT\n")
                MainView.show_players_list(cls.players)

            elif choice == 5:
                (new_tournament) =\
                    Tournament(len(cls.tournaments) + 1, 'Ta', 'Paris',
                               '12/07/2023', '12/07/2023', 'Director')
                cls.tournaments.append(new_tournament)
                (new_player1) =\
                    Player(len(cls.players) + 1, 'AB12345', 'charlie1',
                           'dupond1', '12/07/1989', 'male')
                cls.players.append(new_player1)
                (new_player2) =\
                    Player(len(cls.players) + 1, 'AB12346', 'charlie2',
                           'dupond2', '12/07/1989', 'male')
                cls.players.append(new_player2)
                (new_player3) =\
                    Player(len(cls.players) + 1, 'AB12347', 'charlie3',
                           'dupond3', '12/07/1989', 'male')
                cls.players.append(new_player3)
                (new_player4) =\
                    Player(len(cls.players) + 1, 'AB12348', 'charlie4',
                           'dupond4', '12/07/1989', 'male')
                cls.players.append(new_player4)
                (new_player5) =\
                    Player(len(cls.players) + 1, 'AB12349', 'charlie5',
                           'dupond5', '12/07/1989', 'male')
                cls.players.append(new_player5)
                (new_player6) =\
                    Player(len(cls.players) + 1, 'AB12310', 'charlie6',
                           'dupond6', '12/07/1989', 'male')
                cls.players.append(new_player6)
                (new_player7) =\
                    Player(len(cls.players) + 1, 'AB12311', 'charlie7',
                           'dupond7', '12/07/1989', 'male')
                cls.players.append(new_player7)
                (new_player8) =\
                    Player(len(cls.players) + 1, 'AB12312', 'charlie8',
                           'dupond8', '12/07/1989', 'male')
                cls.players.append(new_player8)
                print("Tournament and Players created")

            elif choice == 6:
                # resume_data = MainView.resume_tournament_view
                # print('Final score', resume_data)
                print("End of Tournament", new_tournament.ID)
                max_key = max(cls.round_players, key=cls.round_players.get)
                # max method reserved to find the maximum number
                (MainController.winner) =\
                    new_tournament.players[max_key-1].first_name
                print("the winner of tournament is player =",
                      MainController.winner)
=======

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
>>>>>>> bd9e9df4fc362006e5057ee6501f4d122e2eb171

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
