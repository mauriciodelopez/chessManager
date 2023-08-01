import json
from controllers.tournamentController import TournamenController
from controllers.playerController import PlayerController
from controllers.roundController import RoundController
from models.tournament import Tournament
from models.players import Player
from models.round import Round
from models.matches import Matche
from views.reportView import ReportView


class ReportController:

    @staticmethod
    def generate_reports():
        data = ReportController.load_data()
        print(data)
        if not data :
            return "error"
        while True:
            choice = ReportView.menu()

            if choice == 1:
                ReportView.print_list_of_players(data["players"])
            elif choice == 2:
                ReportView.print_list_of_tournaments(data["tournaments"])
            elif choice == 3:
                ReportView.print_tournament_by_id(data["tournaments"])
            elif choice == 4:
                ReportView.print_players_by_tournament(data["tournaments"])
            elif choice == 5:
                ReportView.print_list_of_rounds(data["rounds"])
            elif choice == 6:
                ReportView.print_winner_by_tournament(data.get["winners",[]])
            elif choice == 7:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    # recuperer l'information du JSON FILE
    @staticmethod
    def save_data():

        data = {
                "tournaments": [tournament.to_dict() for tournament in TournamenController.tournaments],
                "players": [player.to_dict() for player in PlayerController.players],
                "winners": TournamenController.winners
                }
        with open("chess.json", 'w') as file:
            json.dump(data, file, indent=4)
    
    @staticmethod
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

                    match_data = r_data["matches"]
                    if match_data: 
                        for m_data in match_data:
                            player1_id = m_data["player1"]
                            player2_id = m_data.get("player2", None)  
                            match_ = Matche(
                                m_data["ID"],
                                m_data["scorePlayer1"],
                                m_data["scorePlayer2"],
                                player1_id,
                                player2_id 
                            )
                            round_.add_matche(match_)

            PlayerController.players = [Player(**p_data) for p_data in data["players"]]

        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error: ", str(e))
