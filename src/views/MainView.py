from datetime import datetime



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
        print('4: get_player')
        print('5: Create round')
        print('6: Create match')
        print('7: resume match')
        print('8: Reports')
        print('9: Default')
        print('0: Exit')
        print("\n__________________________________\n\n")
        
                
        choice= -1
        while(choice < 0 or choice > 9):
            choice = int(input("Enter option: "))
            
        
        return choice

              
    @staticmethod     
    def tournament_view():
        
        inputTournament = input("Enter the name of tournament:  ")
        input_location = input("Enter the town of tournament:  ")
        input_date_start = input("Enter the date of tournament start:  ")
        input_date_end = input("Enter the tournament end date: ")
        input_description = input("Enter description of tournament: ")
        
      
    
        return {
            'name': inputTournament, 
            'location': input_location, 
            'date_start': input_date_start, 
            'date_end': input_date_end, 
            'description': input_description
            }
            
    def round_view():
        date = datetime.now() #
        input_name_round = input("Enter the name of round: ")
        input_round_number = input("Enter the round number: ")
        input_start_time = date.hour, "/", date.day, "/", date.month, "/", date.year
        
                   
        return {
            'name': input_name_round, 
            'round_number': input_round_number, 
            'start_time': input_start_time 
                }
    
    
    @staticmethod
    def resume_match_view():
        input_ID = input("please enter the ID of the match you would finisch : ")
        input_score_player1 = input("Please enter the score of player1 (0=lost, 1=winner, 0,5=stalemate):  ")
        input_score_player2 = input("Please enter the score of player2 (0=lost, 1=winner, 0,5=stalemate):  ")
        
        if input_score_player1== 1 :    
            print('The winner is player1')
                
        elif input_score_player2 == 1 : 
            print("The winner is player2")
                
        else: print("stalemate")
        
        return input_score_player1,input_score_player2, input_ID

    
       
    @staticmethod
    def resume_tournament_view():
        input_score = input("Please enter the score of the completed match :  ")
        
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
        
    @classmethod
    def get_player(self):
        input_player_id = int(input("Insert the id of player: "))  
        
        return input_player_id -1
        
    @staticmethod    
    def show_players_list(players_list):
    
        players_list=sorted(players_list, key=lambda x: x.first_name)
        for p in range(0, len(players_list)):
            print(f" {players_list[p]}")
            
    
    
    
    @staticmethod    
    def show_tournament_list(tournament_list):
        
        tournament_list =sorted(tournament_list, key=lambda x: x.name)
        for t in range(0, len(tournament_list)):
            print(f"{tournament_list[t]}")
            
            
            
        
            
    

