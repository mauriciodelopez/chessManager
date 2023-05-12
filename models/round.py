#un round est compose des plusiers maths exemple : 1 round : 4 maths donc 8 joueurs

class Round:
    def __init__(self, name, round_number,matches_list=[], start_time="",end_time=""):
        self.name = name
        self.round_number = int(round_number)
        self.matches_list = matches_list
        self.start_time = start_time
        self.end_time = end_time
