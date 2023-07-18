import json


class MainView:

    @classmethod
    def showMenu(cls):
        print("\n__________________________________")
        print("             WELCOME")
        print("__________________________________\n")
        print('Please select a action:\n')
        print('1: Create a tournament')
        print('2: Create players')
        print('3: Get_player to tournament')
        print('4: Reports')
        print('5: Generate JSON file')
        print('0: Exit')
        print("\n__________________________________\n\n")

        choice = -1
        while (choice < 0 or choice > 5):
            choice = int(input("Enter option: "))

        return choice

    @staticmethod
    def generateJson(tournament_list, winner):
        tournaments_data = []

        for tournament in tournament_list:
            rounds_data = []
            players_data = []

            for player in tournament.players:

                players_dict = {
                    "Players : " +
                    "ID": player.ID,
                    "first_name": player.first_name,
                    "last_name": player.last_name,
                    "date_of_birth": player. date_of_birth,
                    "gender": player.gender
                                }
                players_data.append(players_dict)

            for round_ in tournament.rounds:
                matches_data = []
                for match in round_.matches:

                    match_dict = {
                        "ID": match.ID,
                        "scorePlayer1": match.scorePlayer1,
                        "scorePlayer2": match.scorePlayer2,
                        "ID player1": match.player1,
                        "ID player2": match.player2,
                        "color_player1": match.color_player1,
                        "color_player2": match.color_player2
                                }
                    matches_data.append(match_dict)

                rounds_dict = {
                    "name": round_.name,
                    "round_number": round_.round_number,
                    "start_time": round_.start_time,
                    "end_time": round_. end_time,
                    "matches": matches_data
                            }
                rounds_data.append(rounds_dict)

            tournament_dict = {
                "Tournament : " + 'id': tournament.ID,
                'name': tournament.name,
                'location': tournament.location,
                'number_rounds': tournament.number_rounds,
                'description': tournament.description,
                'list of players': players_data,
                'list of rounds': rounds_data,
                'The winner is': winner[tournament.ID-1]}
            tournaments_data.append(tournament_dict)

        with open("chess.json", 'w') as file:

            json.dump(tournaments_data, file, indent=4)
