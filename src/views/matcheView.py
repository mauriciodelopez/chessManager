from views.MainView import MainView

class MatcheView():

    @staticmethod
    def resume_match_view(match, players_list):
        id_player = match.player1-1
        id_player2 = match.player2-1
        print("\nMatch", match)
        (message) =\
            f"Please enter the score of {players_list[id_player].first_name}"
        (input_score) =\
            MainView.validate_score(message +
                        " (0=lost, 1=winner, 0.5=stalemate) of match #  ")

        input_score_player1 = input_score

        if input_score_player1 == 1.0:
            input_score_player2 = 0.0
            print('The winner is player1 ', players_list[id_player].first_name)

        elif input_score_player1 == 0.0:
            input_score_player2 = 1.0
            print("The winner is player2 ",
                  players_list[id_player2].first_name)

        elif input_score_player1 == 0.5:
            input_score_player2 = 0.5
            print("stalemate")
        else:
            print("ERROR!")

        print("\nMatch ended")
        return input_score_player1, input_score_player2,
