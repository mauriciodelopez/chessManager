import random

class Player:
    def __init__(self, ID, national_ID, first_name, last_name, date_of_birth, gender):
        self.ID = ID
        self.national_ID = national_ID
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        
        
    def __str__(self):
        
       return (f"\nplayer#{self.ID} "\
                f"\n national_ID = {self.national_ID}"\
                f"first_name = {self.first_name}, "\
                f"last_name = {self.last_name}, "\
                f"date_of_birth = {self.date_of_birth}, "\
                f"gender = {self.gender}, "\
                )        
    
     