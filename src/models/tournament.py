class Tournament():

    def __init__(self, ID, name, location, date_start, date_end, description):
        self.ID = ID
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.number_rounds = 4
        self.rounds = []
        self.players = []
        self.description = description

    def __str__(self):
        round_str = "\n\n".join(str(round) for round in self.rounds)

        return f" \n\nDETAILS OF TOURNAMENT # {self.ID}:\n " \
            f"name =  {self.name}, " \
            f"location = {self.date_start}, " \
            f"date_start = {self.date_start}, " \
            f"date_end = {self.date_end}, " \
            f"description = {self.description}, "\
            f"\n\nROUNDS OF TOURNAMENT:\n  {round_str}, "

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)
