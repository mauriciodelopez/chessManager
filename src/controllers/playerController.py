from views.MainView import MainView
from models.players import Player


class PlayerController:
    
    @classmethod
    def createPlayer(cls):
        player_data = MainView.newplayer_view()
        new_player = Player(
            len(cls.players) + 1,
            player_data['national_ID'],
            player_data['first_name'],
            player_data['last_name'],
            player_data['date_of_birth'],
            player_data['gender'])

        cls.players.append(new_player)
    
    @classmethod    
    def showplayer(cls):
        print("\nPlAYERS OF TOURNAMENT\n")
        MainView.show_players_list(cls.players)