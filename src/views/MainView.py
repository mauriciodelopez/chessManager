from datetime import datetime


class MainView:

    @classmethod
    def showMenu(cls):
        
        print("\n______________________________")
        print("           MAIN MENU")
        print("______________________________\n")
        print("Please select an action:\n")
        print("1. Create Tournament")
        print("2. Create Players")
        print("3. Add Players to Tournament")
        print("4. Create Rounds")
        print("5. Create Matches")
        print("6. Reports")
        print("7. Save Data (JSON)")
        print("8. Load Data (JSON)")
        print("0. Exit")
        print("\n______________________________\n\n")

        choice = -1
        while (choice < 0 or choice > 8):
            choice = cls.validate_int("Enter option: ")

        return choice

    def validate_int(prompt):
        while True:
            try:
                user_input = int(input(prompt))
                return user_input
            except ValueError:
                print("error please insert a number")

    def validate_date(prompt):
        while True:
            try:
                date_str = input(prompt)
                user_input = datetime.strptime(date_str, "%d/%m/%Y")
                return (user_input.strftime("%d/%m/%Y"))
            except ValueError:
                print("error, insert the valide date format dd/mm/yyyy ")

    def validate_yes(prompt):
        while True:

            user_input = input(prompt).lower()
            if user_input == "y":
                return True
            elif user_input == "n":
                return False
            else:
                print("Please insert = y or n")
    @staticmethod
    def validate_list(prompt):
        while True:
            try:
                user_input = input(prompt)
                id_list = [int(item.strip()) for item in user_input.split(",")]
                return id_list
            except ValueError:
                print("Error: Invalid input. Please enter a comma-separated list of integers.")


    def validate_score(prompt):
        while True:
            try:
                user_input = float(input(prompt))
                if user_input not in [0, 0.5, 1]:
                    raise ValueError
                return user_input
            except ValueError:
                print("Error please insert 0, 0.5, 1 ")
