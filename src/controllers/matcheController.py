from views.MainView import MainView
from models.matches import Matche
from controllers.playerController import PlayerController
from views.matcheView import MatcheView


class MatcheController:

    

    @staticmethod
    def resume_match (match,round_players):
        (score_player1, score_player2) =\
            MatcheView.resume_match_view(match, PlayerController.players)
        match.scorePlayer1 += score_player1
        match.scorePlayer2 += score_player2
        round_players[match.player1] += match.scorePlayer1
        round_players[match.player2] += match.scorePlayer2

    @staticmethod
    def create_match(new_round, score1, score2, player1, player2):
        new_match = Matche(len(new_round.matches) + 1, score1, score2, player1, player2)
        new_round.add_matche(new_match)
