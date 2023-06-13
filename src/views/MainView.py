
class MainView:
    
    @classmethod   
    def showMenu(cls):
        print("\n__________________________________")
        print("             WELCOME")
        print("__________________________________\n")
        print('Please select a action:\n')
        print('1: Create a tournament go view #2')
        print('2: Resume tournament go view #8')
        print('3: Create players go view #5' )
        print('4: Create round')
        print('5: Create match')
        print('6: Reports go view #7')
        print('0: Exit')
        print("\n__________________________________\n\n")
        
                
        choice= -1
        while(choice < 0 or choice > 6):
            choice = int(input("Enter option: "))
            
        
        return choice

              
    @staticmethod     
    def tournament_view():
        inputTournament = input("Enter the name of tournament:  ")
        input_location = input("Enter the town of tournament:  ")
        input_date_start = input("Enter the date of tournament start:  ")
        input_date_end = input("Enter the tournament end date: ")
        #input_rounds = input("Enter the number of rounds: ")
        input_time_control = input("Enter the time_control: ")
        input_description = input("Enter description of tournament: ")
        
      
    
        return {
            'name': inputTournament, 
            'location': input_location, 
            'date_start': input_date_start, 
            'date_end': input_date_end,
            #'number_rounds': input_rounds, 
            'time_control': input_time_control, 
            'description': input_description
            }
            
    def round_view():
        input_name_round = input("Enter the name of round: ")
        input_round_number = input("Enter the round number: ")
        input_start_time = input("Enter the start time: ")
        input_end_time = input("Enter the end time: ")
                   
        return {
            'name': input_name_round, 
            'round_number': input_round_number, 
            'start_time': input_start_time, 
            'end_time': input_end_time
                }
    
    def match_view():
        input_scorePlayer1 = input("Enter the score of player 1: ")
        input_scorePlayer2 = input("Enter the score of player 2: ")
        input_player1= input("Enter the name of player 1: ")
        input_player2= input("Enter the name of player 2: ")
        
        return {
            'scorePlayer1': input_scorePlayer1,
            'scorePlayer2' : input_scorePlayer2,
            'player1': input_player1,
            'player2': input_player2          
                }
        
    @staticmethod
    def resume_tournament_view():
        input_score = input("Please enter the score of the completed match:  ")
        
        return input_score   
    
    @classmethod
    def newplayer_view(cls):
        input_first_name = input("Insert first_name: ")
        input_last_name = input("Insert the last name of player:  ")
        input_date_of_birth = input("Insert the date_of_birth: ")
        input_gender = input("Insert gender of player: ")
        
        return {
            'first_name': input_first_name, 
            'last_name': input_last_name, 
            'date_of_birth': input_date_of_birth, 
            'gender': input_gender
            }
        
        
        
    @staticmethod    
    def show_players_list(players_list):
    
        players_list=sorted(players_list, key=lambda x: x.first_name)
        for p in players_list:
            print("ID: ", p.ID)
            print("Name: ",p.first_name)
            print("Last Name: ",p.last_name)
            print("Date Birth: ", p.date_of_birth)
            print("Gender: ",p.gender)
            
    
    
    
    @staticmethod    
    def show_tournament_list(tournament_list):
        
        tournament_list =sorted(tournament_list, key=lambda x: x.name)
        for t in tournament_list:
            print("ID: ", t.ID)
            print("Name: ",t.name)
            print("Location: ",t.location)
            print("Date Start: ",t.date_start)
            print("Date End: ",t.date_end)
            print("Number Rounds: ",t.number_rounds)
            print("Time Control: ",t.time_control)
            print("Description: ",t.description)
            print("Players_ name: ",t.players [0].first_name)
            print("Rounds_name: ",t.rounds [0].name)
            print("Matches_score:",t.rounds [0].matches[0].scorePlayer1)
            
        
            
    

