from views.MainView import MainView
from controllers.tournamentController import TournamenController
from controllers.playerController import PlayerController
from controllers.roundController import RoundController
from views.playerView import PlayerView
from controllers.reportController import ReportController


class MainController:

    selected = []

    @classmethod
    def main_menu(cls):
        ReportController.load_data()
        choice = None
        while (choice != 0):
            choice = MainView.showMenu()
            # creation of new tournament
            if choice == 1:
                TournamenController.create_tournament()
                ReportController.save_data()
            # create player
            elif choice == 2:
                PlayerController.createPlayer()
                ReportController.save_data()
            # add player of the tournament from default db
            elif choice == 3:
                if TournamenController.tournaments and PlayerController.players:
                    incomplete_tournaments = [tournament for tournament
                                              in TournamenController.tournaments if not tournament.rounds]
                    if incomplete_tournaments:
                        print("Incomplete Tournaments:")
                        for tournament in incomplete_tournaments:
                            print(f"Tournament ID: {tournament.ID}, Name: {tournament.name}")

                        tournament_id_choice = MainView.validate_int("Select a tournament ID to complete: ")
                        selected_tournament = next((tournament for tournament in incomplete_tournaments
                                                    if tournament.ID == tournament_id_choice), None)

                        if selected_tournament:
                            selected_players = []
                            PlayerController.showplayer()
                            print("\nPlease, insert 8 players: ")
                            while len(selected_players) < 8:
                                id = PlayerView.get_player()
                                if id in cls.selected:
                                    print("The ID of the player is repeated.")
                                else:
                                    cls.selected.append(id)
                                    selected_players.append(PlayerController.players[id])
                                    selected_tournament.add_player(PlayerController.players[id])
                                    RoundController.round_players = {player.ID: 0 for player
                                                                     in selected_tournament.players}

                            RoundController.generate_matches(selected_tournament)
                            TournamenController.get_winner(selected_tournament.ID - 1)
                            cls.selected = []

                            ReportController.save_data()
                        else:
                            print("Invalid tournament ID. The selected tournament =\
                                does not exist or has already been completed.")
                    else:
                        print("No incomplete tournaments found.")
                else:
                    print("Error, you must create a tournament and have at least 8 players first.")

            elif choice == 4:
                ReportController.generate_reports()

            elif choice == 0:
                ReportController.save_data()
                print("Exit...")
