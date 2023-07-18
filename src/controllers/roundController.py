from views.MainView import MainView
from models.round import Round
from views.roundView import RoundView
from controllers.matcheController import MatcheController


class RoundController():

    round_players = {}

    @staticmethod
    def create_round():
        round_data = RoundView.round_view()
        new_round = Round(
            round_data['name'],
            round_data['round_number'],
            round_data['start_time']
                        )
        return new_round

    @staticmethod
    def resume_round(new_round):
        end_date = RoundView.resume_round_view()
        new_round.end_time = end_date

    @classmethod
    def generate_matches(cls, tournament):
        for i in range(tournament.number_rounds):
            new_round = cls.create_round()
            tournament.add_round(new_round)
            matche = new_round.get_match_pairing(cls.round_players, len(tournament.rounds))
            print('Match created:', matche)

            for j in range(tournament.number_rounds):
                score1, score2, player1, player2 = matche[j]
                MatcheController.create_match(new_round, score1, score2, player1, player2)

            for match in new_round.matches:
                MatcheController.resume_match(match, cls.round_players)

            cls.resume_round(new_round)
