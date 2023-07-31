from models.matches import Matche
from views.matcheView import MatcheView
class MatcheController:

    @staticmethod
    def resume_match(match, round_players,tournament):
        (score_player1, score_player2) = MatcheView.resume_match_view(match, tournament.players)
        match.scorePlayer1 += score_player1
        match.scorePlayer2 += score_player2
        round_players[match.player1] = match.scorePlayer1
        round_players[match.player2] = match.scorePlayer2
        

    @staticmethod
    def create_match(new_round, score1, score2, player1, player2):
        new_match = Matche(len(new_round.matches) + 1, score1, score2, player1, player2)
        new_round.add_matche(new_match)
        return new_match
    
    @staticmethod
    def create_matches_for_round(new_round, round_players):
        matches = new_round.get_match_pairing(round_players, new_round.round_number)
        matches_created = []

        for match in matches:
            score1, score2, player1, player2 = match
            new_match = MatcheController.create_match(new_round, score1, score2, player1, player2)
            matches_created.append(new_match)

        return matches_created