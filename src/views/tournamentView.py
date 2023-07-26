from views.MainView import MainView

class TournamentView():

    @staticmethod
    def tournament_view():

        inputTournament = input("Enter the name of tournament:  ")
        input_location = input("Enter the town of tournament:  ")
        input_date_start = MainView.validate_date("Enter the date of tournament start:  ")
        input_date_end = MainView.validate_date("Enter the tournament end date: ")
        input_number_rounds=4
        input_description = input("Enter description of tournament: ")

        print("tournament created by default")

        return {
            'name': inputTournament,
            'location': input_location,
            'date_start': input_date_start,
            'date_end': input_date_end,
            'number_rounds': input_number_rounds,
            'description': input_description
            }

    @staticmethod
    def show_tournament_list(tournament_list):

        tournament_list = sorted(tournament_list, key=lambda x: x.name)
        for t in range(0, len(tournament_list)):

            print(f"{tournament_list[t]}")
