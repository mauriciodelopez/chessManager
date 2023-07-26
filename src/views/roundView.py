from datetime import datetime
from views.MainView import MainView
import sys


class RoundView():

    @staticmethod
    def round_view():
        date = datetime.now()
        input_name_round = input("Enter the name of round: ")
        input_round_number = MainView.validate_int("Enter the round number: ")
        input_start_time = str(date.strftime('%H:%M:%S,%d/%m/%Y'))
        print("\nRound added to the tournament")

        return {
            'name': input_name_round,
            'round_number': input_round_number,
            'start_time': input_start_time
                }

    @staticmethod
    def resume_round_view():
        date = datetime.now()
        resp = MainView.validate_yes("To end the round, insert 'y': ")
        if resp :
            print("Round ended")
            return str(date.strftime('%H:%M:%S,%d/%m/%Y'))
        else : 
            print("error, please write y to continue")
            sys.exit()
