class Matche():
    def __init__(self, ID, scorePlayer1, scorePlayer2, player1, player2):
        self.ID = ID
        self.scorePlayer1 = scorePlayer1
        self.scorePlayer2 = scorePlayer2
        self.player1 = player1
        self.player2 = player2
        self.color_player1 = "white"
        self.color_player2 = "black"

    def update_scores(self, scorePlayer1, scorePlayer2):
        self.scorePlayer1 += scorePlayer1
        self.scorePlayer2 += scorePlayer2

    def __str__(self):

        return f"\n match # ID = {self.ID}," \
                f"scorePlayer1 = {self.scorePlayer1}, " \
                f"scorePlayer2 = {self.scorePlayer2}, " \
                f"player1 = {self.player1}, " \
                f"player2 = {self.player2}, " \
                f"color_player1 = {self.color_player1}," \
                f"color_player2 = {self.color_player2}, " \


    def to_dict(self):

        return {
            "ID": self.ID,
            "scorePlayer1": self.scorePlayer1,
            "scorePlayer2": self.scorePlayer2,
            "player1": self.player1,
            "player2": self.player2,
            "color_player1": self.color_player1,
            "color_player2": self.color_player2
        }
