from models.players import Player
from views.playerView import PlayerView
from views.MainView import MainView


class PlayerController:

    """create or get default player from database"""

    players = []

    @classmethod
    def createPlayer(cls, national_ID='AB12345', first_name='charlie',
                     last_name='dupond', date_of_birth='12/07/1989', gender='male'):
        option = MainView.validate_yes("to create the default players type 'y' or'n' ")

        if option:
            for i in range(8):
                new_player = Player(
                    len(cls.players) + 1,
                    national_ID,
                    first_name+str(i),
                    last_name+str(i),
                    date_of_birth,
                    gender)
                cls.players.append(new_player)
            print("Default players created")
        else:

            player_data = PlayerView.newplayer_view()
            new_player = Player(
                len(cls.players) + 1,
                player_data['national_ID'],
                player_data['first_name'],
                player_data['last_name'],
                player_data['date_of_birth'],
                player_data['gender'])

            cls.players.append(new_player)
            print("Player created")

    @classmethod
    def showplayer(cls):
        """Display all players of tournament"""
        print("\nPlAYERS OF TOURNAMENT\n")
        PlayerView.show_players_list(cls.players)
    
    @classmethod
    def get_player_by_id(cls, player_id):
        for player in cls.players:
            if player.ID == player_id:
                return player
        return None
