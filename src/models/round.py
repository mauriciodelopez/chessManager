#un round est compose des plusiers maths exemple : 1 round : 4 maths donc 8 joueurs

import random

class Round:
    def __init__(self, name, round_number, start_time="",end_time=""):
        self.name = name
        self.round_number = int(round_number)
        self.matches = []
        self.start_time = start_time
        self.end_time = end_time
        
    def __str__(self):
            match_str = "\n\n".join(str(match) for match in self.matches)
            return  f"\n\n DETAILS OF ROUND:\nname = {self.name}, " \
                    f"round_number = {self.round_number}, " \
                    f"\n\nMATCH OF ROUND {self.round_number}: = {match_str}, " \
                    f"start_time = {self.start_time}, " \
                    f"end_time = {self.end_time}, " \

        
    def add_matche(self, matche):
        self.matches.append(matche)
        
    def get_match_pairing(self,list_of_players):
      
        
        tuple_players = []
        
        random.shuffle(list_of_players)
        
        #from 0 to len logitude of all list of players ,2 its a intervalle to 2 in 2 for exemple
        for i in range(0, len(list_of_players),2):
            player1 = list_of_players[i]
            player2 = list_of_players[i+1]
            match = (player1,player2)
            tuple_players.append(match)
            return match
            
            
        
        
        
        



