from models.tournament import Tournament
from views.MainView import MainView
from controllers.playerController import PlayerController
from controllers.matcheController import MatcheController
from views.tournamentView import TournamentView


class TournamenController():
    tournaments = []
    winners = []

    @classmethod
    def create_tournament(cls, name='Ta', location='12/07/2023', date_start='12/07/2023',
                          date_end='12/07/2023', description='Director'):
        option = input("to create the default tournament type 'y' ")

        if option == 'y':
            new_tournament = Tournament(
                len(cls.tournaments) + 1,
                name,
                location,
                date_start,
                date_end,
                description)
            print("Default tournament created")
        else:
            tournament_data = TournamentView.tournament_view()
            # creation de l'instance de l'objet tournoi
            new_tournament = Tournament(
                len(cls.tournaments) + 1,
                tournament_data['name'],
                tournament_data['location'],
                tournament_data['date_start'],
                tournament_data['date_end'],
                tournament_data['description'])
            print("Tournament created")

        cls.tournaments.append(new_tournament)

    @classmethod
    def show_tournament(cls):
        print("TOURNAMENT\n")
        TournamentView.show_tournament_list(cls.tournaments)

    @classmethod
    def get_winner(cls):
        print("End of Tournament", cls.tournaments[-1].ID)
        max_key = max(MatcheController.round_players, key=MatcheController.round_players.get)
        # max method reserved to find the maximum number
        cls.winners.append(
            PlayerController.players[max_key-1].first_name)
        print("the winner of tournament is player =",
              cls.winners[cls.tournaments[-1].ID-1])