from controllers.tournamentController import TournamenController
from controllers.playerController import PlayerController
from controllers.matcheController import MatcheController
from controllers.roundController import RoundController
from views.MainView import MainView
from models.round import Round
from controllers.reportController import ReportController


class MainController:
    @classmethod
    def main_menu(cls):
        ReportController.load_data()
        while True:
            choice = MainView.showMenu()

            if choice == 1:
                TournamenController.create_tournament()
                ReportController.save_data()

            elif choice == 2:
                PlayerController.createPlayer()
                ReportController.save_data()

            elif choice == 3:
                MainController.add_players_to_tournament()
                ReportController.save_data()

            elif choice == 4:
                MainController.create_rounds()
                ReportController.save_data()

            elif choice == 5:
                MainController.create_matches()
                ReportController.save_data()
            elif choice == 6:
                ReportController.generate_reports()

            elif choice == 7:
                ReportController.save_data()

            elif choice == 8:
                ReportController.load_data()

            elif choice == 9:
                MainController.insert_test_data()

            elif choice == 0:
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")

    @staticmethod
    def add_players_to_tournament():
        tournament_id = MainView.validate_int("Enter the ID of the tournament: ")
        tournament = TournamenController.get_tournament(tournament_id)
        
        if tournament is not None:
            incomplete_rounds = TournamenController.get_incomplete_rounds(tournament)
            if incomplete_rounds:
                print("Incomplete rounds found in the tournament. Please complete the rounds before adding players.")
            else:
                PlayerController.showplayer()
                if tournament:
                    for i in range (8):
                        player_id = MainView.validate_int("Enter the ID of the player to add: ")
                        player = PlayerController.get_player_by_id(player_id)
                        if player is not None:
                            tournament.add_player(player)
                            print(f"Player '{player.first_name}' added to the tournament.")
                        else:
                            print("Invalid player ID. Please enter a valid ID.")
        else:
            print("Tournament not found. Please enter a valid tournament ID.")
    
    
    def create_rounds():
        if TournamenController.tournaments:
            tournament_id = MainView.validate_int("Enter the ID of the tournament: ")
            tournament = TournamenController.get_tournament(tournament_id)

            if tournament:
                if len(tournament.rounds) >= 4:
                    print("Error, you cannot create more than 4 rounds for the selected tournament.")
                    return

                while True:
                    choice = MainView.validate_yes("\nDo you want to create a round? (y/n): ")
                    if choice:
                        new_round = RoundController.create_round()
                        tournament.add_round(new_round)
                        if len(tournament.rounds) >= 4:
                            print("You have created 4 rounds. No more rounds can be created for this tournament.")
                            break
                    else:
                        break

                print("Rounds created successfully.")
                ReportController.save_data()
            else:
                print("Invalid tournament ID. The selected tournament does not exist.")
        else:
            print("Error, you must create a tournament first.")
        
    def create_matches():
        tournament_id = MainView.validate_int("Enter the ID of the tournament: ")
        selected_tournament = TournamenController.get_tournament(tournament_id)

        if selected_tournament and selected_tournament.rounds:
            print(f"Tournament: {selected_tournament.name}")

            # List available rounds for the tournament
            for round_ in selected_tournament.rounds:
                print(f"Round {round_.round_number}: {round_.name}")

            # Check if all rounds have ended before entering the while loop
            all_rounds_ended = all(round_.end_time != "" for round_ in selected_tournament.rounds)

            while not all_rounds_ended:
                try:
                    round_number = MainView.validate_int("Enter the round number to create matches for (0 to exit): ")
                    if round_number == 0:
                        break

                    current_round = selected_tournament.rounds[round_number - 1]

                    if current_round:

                        # Check if the current round has ended
                        if current_round.end_time == "":
                            round_players = {player.ID: 0 for player in selected_tournament.players}
                            match_list = current_round.get_match_pairing(round_players, current_round.round_number)

                            max_matches = len(selected_tournament.players) // 2
                            num_matches_created = len(current_round.matches)

                            while num_matches_created < max_matches:
                                choice = MainView.validate_yes("\nDo you want to create a match? (y/n): ")
                                if choice:
                                    RoundController.generate_matches(selected_tournament, current_round.round_number, round_players, match_list, num_matches_created)
                                    num_matches_created += 1
                                    ReportController.save_data()

                                    if num_matches_created == max_matches:
                                        num_matches_created = 0  # Reset num_matches_created when the round is ended
                                        RoundController.resume_round(current_round)
                                        ReportController.save_data()
                                        break
                                else:
                                    choice_round_end = MainView.validate_yes("\nDo you want to end this round? (y/n): ")
                                    if choice_round_end:
                                        num_matches_created = 0  # Reset num_matches_created when the round is ended
                                        RoundController.resume_round(current_round)
                                        ReportController.save_data()
                                        break
                            # Update the all_rounds_ended variable after finishing the loop
                            all_rounds_ended = all(round_.end_time != "" for round_ in selected_tournament.rounds)
                        else:
                            print(f"Round {round_number} has already ended. Cannot create matches for this round.")
                            TournamenController.get_winner(tournament_id)
                            ReportController.save_data()
                    else:
                        print(f"Invalid round number. Round {round_number} does not exist in the selected tournament.")
                except ValueError:
                    print("Invalid input. Please enter a valid round number.")

            # Tournament end logic here, once all rounds have a final date set
            if all_rounds_ended:
                print("All rounds have been completed. The tournament has ended.")
                TournamenController.get_winner(tournament_id)
                ReportController.save_data()

        else:
            print("No rounds have been created for the selected tournament.")


                
    @staticmethod
    def insert_test_data():
        PlayerController.createPlayer(national_ID='123456', first_name='John', last_name='Doe',
                                       date_of_birth='15/05/1990', gender='M')
        PlayerController.createPlayer(national_ID='987654', first_name='Jane', last_name='Smith',
                                       date_of_birth='20/12/1985', gender='F')

        TournamenController.create_tournament(name='Test Tournament', location='City', date_start='01/01/2023',
                                               date_end='05/01/2023', number_rounds=2, description='Test Director')

        MainController.add_players_to_tournament()

        TournamenController.tournaments[0].rounds.append(Round(name="Test Round 1", round_number=1,
                                                               start_time="01/01/2023 10:00 AM"))
        TournamenController.tournaments[0].rounds.append(Round(name="Test Round 2", round_number=2,
                                                               start_time="02/01/2023 10:00 AM"))

        MatcheController.create_match(tournament=TournamenController.tournaments[0], round_number=1, player1_id=0, player2_id=1, score_player1=1.0, score_player2=0.0)
        MatcheController.create_match(tournament=TournamenController.tournaments[0], round_number=2, player1_id=0, player2_id=1, score_player1=0.5, score_player2=0.5)

        TournamenController.get_winner(0)

