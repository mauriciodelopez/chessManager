class PlayerView():

    @staticmethod
    def newplayer_view():

        input_national_ID = input("Please enter your national ID: ")
        input_first_name = input("Insert first_name: ")
        input_last_name = input("Insert the last name of player:  ")
        input_date_of_birth = input("Insert the date_of_birth: ")
        input_gender = input("Insert gender of player: ")

        return {
            'national_ID': input_national_ID,
            'first_name': input_first_name,
            'last_name': input_last_name,
            'date_of_birth': input_date_of_birth,
            'gender': input_gender
            }

    @staticmethod
    def get_player():
        input_player_id = int(input("Insert the id of player: "))
        print("Player added to the tournament\n ")
        return input_player_id - 1

    @staticmethod
    def show_players_list(players_list):

        players_list = sorted(players_list, key=lambda x: x.first_name)

        for p in range(0, len(players_list)):
            print(f" {players_list[p]}")
