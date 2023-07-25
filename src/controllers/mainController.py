from views.MainView import MainView
from controllers.tournamentController import TournamenController
from controllers.playerController import PlayerController
from controllers.roundController import RoundController
from views.playerView import PlayerView
import json
from models.tournament import Tournament
from models.players import Player
from models.round import Round
from models.matches import Matche
class MainController:
    selected = []

    class Encoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Round):
                return obj.__dict__  
            elif isinstance(obj, Matche):
                return obj.__dict__  
            elif isinstance(obj, Player):
                return obj.__dict__  
            return json.JSONEncoder.default(self, obj)
    
    @classmethod
    def main_menu(cls):
        choice = None
        while (choice != 0):
            choice = MainView.showMenu()
            # creation of new tournament
            if choice == 1:
                TournamenController.create_tournament()
                cls.save_data(cls)
            # create player
            elif choice == 2:
                PlayerController.createPlayer()
                cls.save_data(cls)
            # add player of the tournament from default db
            elif choice == 3:
                PlayerController.showplayer()
                print("\nPlease, insert  8 players: ")
                while len(TournamenController.tournaments[-1].players) < 8:

                    id = PlayerView.get_player()
                    if id in cls.selected:
                        print("the id of player is repeated")
                    else:
                        cls.selected.append(id)
                        TournamenController.tournaments[-1].add_player(PlayerController.players[id])
                        (RoundController.round_players) =\
                            {player.ID: 0 for player in TournamenController.tournaments[-1].players}

                RoundController.generate_matches(TournamenController.tournaments[-1])
                TournamenController.get_winner()
                cls.selected = []

                # resume_data = MainView.resume_tournament_view
                # print('Final score', resume_data)

                cls.save_data(cls)

            elif choice == 4:
                cls.generate_reports()
                
            elif choice == 5:
                cls.generate_json()

            elif choice == 0:
                cls.save_data(cls)
                print("Exit...")

    def generate_reports():

        print("\nList of players: ")
        for player in PlayerController.players:
            print(player)
        
        print("\nList of tournaments: ")
        for tournament in TournamenController.tournaments:
            print(tournament)

        print ("\n Name and Date of tournament")
        tournament_id=MainView.validate_int("Insert id of tournament: ")
        if tournament_id>0 and tournament_id <=len(TournamenController.tournaments):
            tournament=TournamenController.tournaments [tournament_id-1]
            print(tournament)
        else:
            print("The tournament has not been created")

        
        if len (TournamenController.tournaments)>0:
            print("\nList of players by tournament")
            tournament_id=MainView.validate_int("Insert the id of tournament: ")
            if tournament_id>0 and tournament_id<=len(TournamenController.tournaments):
                tournament=TournamenController.tournaments[tournament_id-1]
                for player in tournament.players:
                    print(player)
            else:
                print("The tournament has not been created")

        if len(TournamenController.tournaments)>0:
            print("\nList of rounds")
            tournament_id=MainView.validate_int("Insert id of tournament: ")
            if tournament_id>0 and tournament_id<=len(TournamenController.tournaments):
                tournament=TournamenController.tournaments[tournament_id-1]
                for round in tournament.rounds:
                    print(round)
            else:
                print("The tournament has not been created")

    def save_data(cls):
        data={
            "tournaments":[tournament.__dict__ for tournament in TournamenController.tournaments],
            "players":[player.__dict__ for player in PlayerController.players],
            "round_players": RoundController.round_players
            }
        with open ("chess.json",'w') as file:
            json.dump(data,file,indent=4,cls=cls.Encoder)
    
    def load_data():
        try:
            with open("chess.json",'r') as file:
                data=json.load(file)
            print("file",data)
            TournamenController.tournaments=[Tournament(**t_data) for t_data in data["tournaments"]]
            PlayerController.players=[Player(**p_data) for p_data in data["players"]]            
            RoundController.round_players=data["round_players"]
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error ",str(e))

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

        with open("chess_json.json", 'w') as file:

            json.dump(tournaments_data, file, indent=4)
        
        


