
from views.MainView import MainView


class ReportView:

    @staticmethod
    def print_list_of_players(players):
        print("\nList of players:")
        for player in players:
            print(player)

    @staticmethod
    def print_list_of_tournaments(tournaments):
        print("\nList of tournaments:")
        for tournament in tournaments:
            print(tournament)

    @staticmethod
    def print_tournament_by_id(tournaments):
        print("\nName and Date of tournament")
        tournament_id = MainView.validate_int("Insert the id of the tournament: ")
        if 1 <= tournament_id <= len(tournaments):
            tournament = tournaments[tournament_id - 1]
            print(tournament)
        else:
            print("The tournament has not been created.")

    @staticmethod
    def print_players_by_tournament(tournaments):
        if len(tournaments) > 0:
            print("\nList of players by tournament")
            tournament_id = MainView.validate_int("Insert the id of the tournament: ")
            if 1 <= tournament_id <= len(tournaments):
                tournament = tournaments[tournament_id - 1]
                for player in tournament.players:
                    print(player)
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
                for round in tournament.rounds:
                    print(round)
            else:
                print("The tournament has not been created.")
        else:
            print("No tournaments found. You must create a tournament first.")

    def print_winner_by_tournament(tournaments, winners):
        tournament_id = MainView.validate_int("Insert the id of the tournament: ")
        if 1 <= tournament_id <= len(tournaments):
            print(winners[tournament_id - 1])
        else:
            print("The tournament has not been created.")

    def menu():
        print("\nMenu Options:")
        print("1. List of players")
        print("2. List of tournaments")
        print("3. Name and Date of tournament")
        print("4. List of players by tournament")
        print("5. List of rounds by tournament")
        print("6. Winner by tournament")
        print("7. Exit")

        choice = MainView.validate_int("Select an option: ")
        return choice
