class Tournament():

    def __init__(self, ID, name, location, date_start, date_end, number_rounds, description):
        self.ID = ID
        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.number_rounds = number_rounds
        self.rounds = []
        self.players = []
        self.description = description

    def __str__(self):

        return f" \n\nDETAILS OF TOURNAMENT # {self.ID}:\n " \
            f"name =  {self.name}, " \
            f"location = {self.date_start}, " \
            f"date_start = {self.date_start}, " \
            f"date_end = {self.date_end}, " \
            f"number_rounds = {self.number_rounds}, " \
            f"description = {self.description}, "

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)

    def to_dict(self):
        return {
            "ID": self.ID,
            "name": self.name,
            "location": self.location,
            "date_start": self.date_start,
            "date_end": self.date_end,
            "number_rounds": self.number_rounds,
            "rounds": [round.to_dict() for round in self.rounds],
            "players": [player.to_dict() for player in self.players],
            "description": self.description
        }
