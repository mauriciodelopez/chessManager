

class Matche():
    def __init__(self, ID, scorePlayer1, scorePlayer2, player1, player2):
        self.ID = ID
        self.scorePlayer1 = scorePlayer1
        self.scorePlayer2 = scorePlayer2
        self.player1 = player1
        self.player2 = player2
    
    def __str__(self):

            return  f"\n match # ID = {self.ID},"\
                    f"scorePlayer1 = {self.scorePlayer1}, " \
                    f"scorePlayer2 = {self.scorePlayer2}, " \
                    f"{self.player1}, " \
                    f"{self.player2}, " \
                        
    
    