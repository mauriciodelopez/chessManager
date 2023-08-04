from views.MainView import MainView


class ReportView:

    @staticmethod
    def print_list_of_players(players):
        if not players:
            print("No tournaments found")
        print("\nList of players:")
        for player in players:
            print("ID: ",player["ID"])
            print("National ID: ",player["national_ID"])
            print("First_name: ",player["first_name"])
            print("Last_name: ",player["last_name"])
            print("Date of birth: ",player["date_of_birth"])
            print("Gender: ",player["gender"])
            print("\n_____________________________________________\n")
    @staticmethod
    def print_list_of_tournaments(tournaments):
        if not tournaments:
            print("No tournaments found")
        else:
            print("\nList of tournaments:\n")
            for tournament in tournaments:
                print("ID: ",tournament["ID"])
                print("Name: ",tournament["name"])
                print("Location: ",tournament["location"])
                print("Date start",tournament["date_start"])
                print("Date end",tournament["date_end"])
                print("Number rounds",tournament["number_rounds"])
                print("\n_____________________________________________\n")

    @staticmethod
    def print_tournament_by_id(tournaments):
        print("\nName and Date of tournament")
        tournament_id = MainView.validate_int("Insert the id of the tournament: ")
        if 1 <= tournament_id <= len(tournaments):
            tournament = tournaments[tournament_id - 1]
            print("ID: ",tournament["ID"])
            print("Name: ",tournament["name"])
            print("Location: ", tournament["location"])
            print("Date start", tournament["date_start"])
            print("Date end",tournament["date_end"])
            print("Number rounds",tournament["number_rounds"])
            print("\n_____________________________________________\n")
        else:
            print("The tournament has not been created.")

    @staticmethod
    def print_players_by_tournament(tournaments):
        if len(tournaments) > 0:
            print("\nList of players by tournament")
            tournament_id = MainView.validate_int("Insert the id of the tournament: ")
            if 1 <= tournament_id <= len(tournaments):
                tournament = tournaments[tournament_id - 1]
                if not tournament["players"]:
                    print("No players found")
                else:
                    ReportView.print_list_of_players(tournament["players"])
            else:
                print("The tournament has not been created.")
        else:
            print("No tournaments found. You must create a tournament first.")

    @staticmethod
    def print_list_of_rounds(tournaments):
        if len(tournaments) > 0:
            print("\nList of rounds")
            tournament_id = MainView.validate_int("Insert the id of the tournament: ")
            if 1 <= tournament_id <= len(tournaments):
                tournament = tournaments[tournament_id - 1]
                if not tournament["rounds"]:
                    print("No rounds found")
                else:
                    for round in tournament["rounds"]:
                        print("Name: ",round["name"])
                        print("Round_number: ",round["round_number"])
                        print("Start_time: ",round["start_time"])
                        print("End_time: ",round["end_time"])
                        print("\n_____________________________________________\n")
            else:
                print("The tournament has not been created.")
        else:
            print("No tournaments found. You must create a tournament first.")
    
    def print_list_of_matches(tournaments):
        if len(tournaments) > 0:
            print("\nList of rounds")
            tournament_id = MainView.validate_int("Insert the id of the tournament: ")
            if 1 <= tournament_id <= len(tournaments):
                tournament = tournaments[tournament_id - 1]
                round_id = MainView.validate_int("Insert the id of the round: ")
                if 1 <= round_id <= len(tournament['rounds']):
                    round = tournament['rounds'][round_id - 1]
                    if not round["matches"]:
                        print("No matches found")
                    else:
                        for match in round["matches"]:
                            print("ID: ",match["ID"])
                            print("Score Player1: ",match["scorePlayer1"])
                            print("Score Player2: ",match["scorePlayer2"])
                            print("Player 1: ",match["player1"])
                            print("Player 2: ",match["player2"])
                            print("Color Player1: ",match["color_player1"])
                            print("Color Player2: ",match["color_player2"])
                            print("\n_____________________________________________\n")
           
                else:
                    print("The round has not been created.")
            else:
                print("The tournament has not been created.")
        else:
            print("No tournaments found. You must create a tournament first.")



    def print_winner_by_tournament(tournaments, winners):
        tournament_id = MainView.validate_int("Insert the id of the tournament: ")
        if winners :
            if 1 <= tournament_id <= len(tournaments):
                print(winners[tournament_id - 1])
            else:
                print("The tournament has not been created.")
        else:
            print("The tournament it's not finish yet ")        

    def menu():
        print("\nMenu Options:")
        print("1. List of players")
        print("2. List of tournaments")
        print("3. Name and Date of tournament")
        print("4. List of players by tournament")
        print("5. List of rounds by tournament")
        print("6. List of matches by round")
        print("7. Winner by tournament")
        print("8. Exit")

        choice = MainView.validate_int("\nSelect an option: ")
        return choice
