class Round:
    def __init__(self, name, round_number,matches_list=[], start_time="",end_time=""):
        self.name = name
        self.round_number = int(round_number)
        self.matches_list = matches_list
        self.start_time = start_time
        self.end_time = end_time
