import random
from itertools import cycle


class Round:

    def __init__(self, name, round_number, start_time="", end_time=""):
        self.name = name
        self.round_number = int(round_number)
        self.matches = []
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"\n ROUND #{self.round_number}:\n name = {self.name}, "\
            f"start_time = {self.start_time}, "\
            f"end_time = {self.end_time}, "

    def add_matche(self, matche):
        self.matches.append(matche)

    def to_dict(self):
        return {
            "name": self.name,
            "round_number": self.round_number,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": [match.to_dict() for match in self.matches]
        }

    @staticmethod
    def get_match_pairing(round_players, idx_round):
        lista = list(round_players.items())
        if idx_round == 1:
            random.shuffle(lista)
        else:
            lista = sorted(lista, key=lambda x: x[1], reverse=True)

        match_list = []
        player_list = cycle(lista)

        while len(match_list) < len(lista) // 2:
            player1, score1 = next(player_list)
            player2, score2 = next(player_list)

            match = (score1, score2, player1, player2)
            match_list.append(match)

        return match_list
