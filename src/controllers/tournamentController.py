from models.tournament import Tournament
from controllers.playerController import PlayerController
from views.tournamentView import TournamentView
from controllers.roundController import RoundController
from views.MainView import MainView


class TournamenController():
    tournaments = []
    winners = []

    @classmethod
    def create_tournament(cls, name='Ta', location='Paris', date_start='12/07/2023',
                          date_end='12/07/2023', number_rounds=4, description='Director'):
        option = MainView.validate_yes("to create the default tournament type 'y' or 'n' ")

        if option:
            new_tournament = Tournament(
                len(cls.tournaments) + 1,
                name,
                location,
                date_start,
                date_end,
                number_rounds,
                description)
            print("Default tournament created")
        else:
            tournament_data = TournamentView.tournament_view()
            new_tournament = Tournament(
                len(cls.tournaments) + 1,
                tournament_data['name'],
                tournament_data['location'],
                tournament_data['date_start'],
                tournament_data['date_end'],
                tournament_data['number_rounds'],
                tournament_data['description'])
            print("Tournament created")

        cls.tournaments.append(new_tournament)

    @classmethod
    def show_tournament(cls):
        print("TOURNAMENT\n")
        TournamentView.show_tournament_list(cls.tournaments)

    @classmethod
    def get_winner(cls, tournament_id):
        selected_tournament = cls.get_tournament(tournament_id)
        if selected_tournament:
            print("End of Tournament", selected_tournament.ID)

            player_scores = {}
            for player in selected_tournament.players:
                player_scores[player.ID] = 0

            for round in selected_tournament.rounds:
                for match in round.matches:
                    player1_id = match.player1
                    player2_id = match.player2
                    score1 = match.scorePlayer1
                    score2 = match.scorePlayer2

                    player_scores[player1_id] += score1
                    player_scores[player2_id] += score2

            if player_scores:
                max_score_player_id = max(player_scores, key=player_scores.get)
                cls.winners.append(PlayerController.get_player_by_id(max_score_player_id).first_name)
                print("Tournament winner:", cls.winners[-1])
            else:
                print("No winner found for Tournament", selected_tournament.ID)
        else:
            print("Tournament not found")

    @classmethod
    def update_rounds(cls, tournament_id):
        selected_tournament = cls.get_tournament(tournament_id)
        if selected_tournament:
            for round_ in selected_tournament.rounds:
                RoundController.resume_round(round_)

    @classmethod
    def get_tournament(cls, tournament_id):
        (selected_tournament) =\
              next((tournament for tournament in cls.tournaments if tournament.ID == tournament_id), None)
        return selected_tournament

    @classmethod
    def get_complete_rounds(cls, tournament_id):
        tournament = cls.get_tournament(tournament_id)
        if tournament is not None:
            complete_rounds = [round_ for round_ in tournament.rounds if round_.end_time != ""]
            return complete_rounds
        else:
            print("Tournament not found.")
            return []

    def get_incomplete_rounds(tournament):
        incomplete_rounds = []
        for round_ in tournament.rounds:
            if round_.end_time == "":
                incomplete_rounds.append(round_)
        return incomplete_rounds
