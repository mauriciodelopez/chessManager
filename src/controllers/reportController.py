
import json
from controllers.tournamentController import TournamenController
from controllers.playerController import PlayerController
from controllers.roundController import RoundController
from models.tournament import Tournament
from models.players import Player
from models.round import Round
from views.reportView import ReportView


class ReportController:

    def generate_reports():
        while True:
            choice = ReportView.menu()

            if choice == 1:
                ReportView.print_list_of_players(PlayerController.players)
            elif choice == 2:
                ReportView.print_list_of_tournaments(TournamenController.tournaments)
            elif choice == 3:
                ReportView.print_tournament_by_id(TournamenController.tournaments)
            elif choice == 4:
                ReportView.print_players_by_tournament(TournamenController.tournaments)
            elif choice == 5:
                ReportView.print_list_of_rounds(TournamenController.tournaments)
            elif choice == 6:
                ReportView.print_winner_by_tournament(TournamenController.tournaments, TournamenController.winners)
            elif choice == 7:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    # recuperer l'information du JSON FILE
    def save_data():

        data = {
                "tournaments": [tournament.to_dict() for tournament in TournamenController.tournaments],
                "players": [player.to_dict() for player in PlayerController.players],
                "winners": TournamenController.winners
                }
        with open("chess.json", 'w') as file:
            json.dump(data, file, indent=4)

    def load_data():
        try:
            with open("chess.json", 'r') as file:
                data = json.load(file)

            TournamenController.winners = data.get("winners", [])
            tournaments_data = data["tournaments"]
            TournamenController.tournaments = []
            for t_data in tournaments_data:
                tournament = Tournament(
                    t_data["ID"],
                    t_data["name"],
                    t_data["location"],
                    t_data["date_start"],
                    t_data["date_end"],
                    t_data["number_rounds"],
                    t_data["description"]
                )
                TournamenController.tournaments.append(tournament)

                players_data = t_data["players"]
                for p_data in players_data:
                    player = Player(
                        p_data["ID"],
                        p_data["national_ID"],
                        p_data["first_name"],
                        p_data["last_name"],
                        p_data["date_of_birth"],
                        p_data["gender"]
                    )
                    tournament.add_player(player)

                rounds_data = t_data["rounds"]
                for r_data in rounds_data:
                    round_ = Round(
                        r_data["name"],
                        r_data["round_number"],
                        r_data["start_time"],
                        r_data["end_time"]
                    )
                    tournament.add_round(round_)

            PlayerController.players = [Player(**p_data) for p_data in data["players"]]

            RoundController.round_players = data["round_players"]
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error: ", str(e))
