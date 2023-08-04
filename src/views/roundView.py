from datetime import datetime
from views.MainView import MainView
import sys


class RoundView():

    @staticmethod
    def round_view():
        input_name_round = input("Enter the name of round: ")
        input_round_number = MainView.validate_int("Enter the round number: ")
        start_time = datetime.now().strftime('%H:%M:%S,%d/%m/%Y')
        
        print("\nRound added to the tournament")

        return {
            'name': input_name_round,
            'round_number': input_round_number,
            'start_time': start_time
        }

    @staticmethod
    def resume_round_view():
        
        print("Round ended")
        return str(datetime.now().strftime('%H:%M:%S,%d/%m/%Y'))

