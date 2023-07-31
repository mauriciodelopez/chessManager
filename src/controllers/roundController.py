from models.round import Round
from views.roundView import RoundView
from controllers.matcheController import MatcheController
class RoundController:
    round_players = {}
    
    @staticmethod
    def create_round():
        round_data = RoundView.round_view()
        new_round = Round(name=round_data['name'], round_number=round_data['round_number'],start_time=round_data['start_time'])

        return new_round

    @staticmethod
    def resume_round(round_):
        end_date = RoundView.resume_round_view()
        round_.end_time = end_date


    
    def generate_matches(tournament, round_number,round_players,match_list,id_matche):
        target_round = tournament.rounds[round_number - 1]
        if not target_round:
            print(f"Round {round_number} not found in the tournament.")
            return

        if target_round.end_time != "":
            print("The round has already been finished. Cannot add new matches.")
            return

        score1, score2, player1, player2 = match_list[id_matche]
        new_match = MatcheController.create_match(target_round, score1, score2, player1, player2)
        MatcheController.resume_match(new_match, round_players,tournament)