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
    
    @classmethod
    def main_menu(cls):
        choice = None
        while (choice != 0):
            choice = MainView.showMenu()
            # creation of new tournament
            if choice == 1:
                TournamenController.create_tournament()
                cls.save_data()
            # create player
            elif choice == 2:
                PlayerController.createPlayer()
                cls.save_data()
            # add player of the tournament from default db
            elif choice == 3:
                cont=0
                if TournamenController.tournaments and PlayerController.players:
                    for i in range(len(TournamenController.tournaments)):
                        if TournamenController.tournaments[i].rounds==[]:
                            print("Tournament # ",TournamenController.tournaments[i].ID,"-",TournamenController.tournaments[i].name)
                            cont+=1
                    for i in range(cont):
                        tournament_choice = MainView.validate_int("Select a tournament: ")
                        if 1 <= tournament_choice <= cont:
                            PlayerController.showplayer()
                            print("\nPlease, insert  8 players: ")
                            while len(TournamenController.tournaments[tournament_choice-1].players) < 8:

                                id = PlayerView.get_player()
                                if id in cls.selected:
                                    print("the id of player is repeated")
                                else:
                                    cls.selected.append(id)
                                    TournamenController.tournaments[tournament_choice-1].add_player(PlayerController.players[id])
                                    (RoundController.round_players) =\
                                        {player.ID: 0 for player in TournamenController.tournaments[tournament_choice-1].players}

                            RoundController.generate_matches(TournamenController.tournaments[tournament_choice-1])
                            TournamenController.get_winner(tournament_choice-1)
                            cls.selected = []

                            cls.save_data()
                            break;
                        else:
                            print("Invalid tournament selection.")
                    else:
                        print("No incomplete tournaments found.")
                else:
                    print("Error, you must create a tournament and at least 8 players first.")
               

            elif choice == 4:
                cls.generate_reports()


            elif choice == 0:
                cls.save_data()
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
    
    def save_data():

        data = {
        "tournaments": [tournament.to_dict() for tournament in TournamenController.tournaments],
        "players": [player.to_dict() for player in PlayerController.players],
    }
        with open("chess.json", 'w') as file:
            json.dump(data, file, indent=4)



    def load_data():
        try:
            with open("chess.json", 'r') as file:
                data = json.load(file)

            # to create instances of tournament from json DATABASE
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

                # Agregamos los jugadores al torneo
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

                # Agregamos los rounds al torneo
                rounds_data = t_data["rounds"]
                for r_data in rounds_data:
                    round_ = Round(
                        r_data["name"],
                        r_data["round_number"],
                        r_data["start_time"],
                        r_data["end_time"]
                    )
                    tournament.add_round(round_)

            # Cargamos la lista de jugadores directamente al PlayerController.players
            PlayerController.players = [Player(**p_data) for p_data in data["players"]]

        except FileNotFoundError:
            print("Archivo no encontrado")
        except Exception as e:
            print("Error: ", str(e))
        


