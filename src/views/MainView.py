from datetime import datetime
import json


class MainView:

    @classmethod
    def showMenu(cls):
        print("\n__________________________________")
        print("             WELCOME")
        print("__________________________________\n")
        print('Please select a action:\n')
        print('1: Create a tournament')
        print('2: Create players')
        print('3: Get_player to tournament')
        print('4: Reports')
        print('0: Exit')
        print("\n__________________________________\n\n")

        choice = -1
        while (choice < 0 or choice > 5):
            choice = cls.validate_int("Enter option: ")

        return choice
    
    @staticmethod
    def validate_int(prompt):
        while True: 
            try:
                user_input = int(input(prompt))
                return user_input
            except ValueError :
                print("error please insert a number")
                
    def validate_date(prompt):
        while True: 
            try:
                date_str = input(prompt)
                user_input = datetime.strptime(date_str, "%d/%m/%Y")
                return (user_input.strftime("%d/%m/%Y"))
            except ValueError :
                print("error, insert the valide date format dd/mm/yyyy ")
                
    def validate_yes(prompt):
        while True: 

            user_input = input(prompt).lower()
            if user_input == "y" :  
                return True
            elif user_input == "n" :
                return False
            else :
                print("Please insert = y or n")
    
    def validate_score(prompt):
        while True:
            try:
                user_input = float(input(prompt))
                if user_input not in [0, 0.5, 1] :  
                    raise ValueError
                return user_input
            except ValueError :
                print("Error please insert 0, 0.5, 1 ")
