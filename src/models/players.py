
class Player:
    def __init__(self, ID, first_name, last_name, date_of_birth, gender):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        
    def __str__(self):
        
       return (f"\n\nDETAILS OF PLAYERS: \nID =  {self.ID}, "\
                f"first_name = {self.first_name}, "\
                f"last_name = {self.last_name}, "\
                f"date_of_birth = {self.date_of_birth}, "\
                f"gender = {self.gender}, "\
                )        
    
    