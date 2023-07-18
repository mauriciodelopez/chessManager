from views.MainView import MainView
from models.round import Round
from views.roundView import RoundView


class RoundController():

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
