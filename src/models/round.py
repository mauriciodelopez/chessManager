#un round est compose des plusiers maths exemple : 1 round : 4 maths donc 8 joueurs

import random

from itertools import cycle

class Round:
    def __init__(self, name, round_number, start_time="",end_time=""):
        self.name = name
        self.round_number = int(round_number)
        self.matches = []
        self.start_time = start_time
        self.end_time = end_time
        
    def __str__(self):
            match_str = "\n".join(str(match) for match in self.matches)
            return  f"\nROUND #{self.round_number}:\nname = {self.name}, " \
                    f"start_time = {self.start_time}, " \
                    f"end_time = {self.end_time}, " \
                    f"\n\nMATCH OF ROUND {self.round_number}:  {match_str}, "

        
    def add_matche(self, matche):
        self.matches.append(matche)
        

    def get_match_pairing(self, round_players, idx_match):
        lista = list(round_players.items())
        lista = sorted(lista, key=lambda x: x[1], reverse=True)
        #print(lista)

        if idx_match == 0:
            random.shuffle(lista)

        match_list = []

        player_count = len(lista)
        mid = player_count // 2

        for i in range(mid):
            player1, score1 = lista[i]
            player2, score2 = lista[player_count - i - 1]

            match = (score1, score2, player1, player2)
            match_list.append(match)

        #print(match_list)
        return match_list
       
            
        #crear un ciclo for con 4 partidos y en el maincontroller se 
            
        
        
        
        
        
        
        



