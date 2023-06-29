from datetime import datetime



class MainView:
    
    @classmethod   
    def showMenu(cls):
        print("\n__________________________________")
        print("             WELCOME")
        print("__________________________________\n")
        print('Please select a action:\n')
        print('1: Create a tournament')
        print('2: Resume tournament')
        print('3: Create players' ) # 1 crear player 
        print('4: Get_player to tournament') # 2 selected player 
        print('5: Create round') 
        print('6: Create match')
        print('7: Resume match') # 
        print('8: Resume round') #
        print('9: Reports')
        print('10: Default')
        print('0: Exit')
        print("\n__________________________________\n\n")
        
                
        choice= -1
        while(choice < 0 or choice > 10):
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
        input_start_time = str(date.strftime('%H:%M:%S,%d/%m/%Y'))
        print("\nRound added to the tournament")
                   
        return {
            'name': input_name_round, 
            'round_number': input_round_number, 
            'start_time': input_start_time
                }
    
    
    @staticmethod
    def resume_match_view(match_list):
        for i in range(0, len(match_list)):
            print(f" {match_list[i]}")
        input_ID = int(input("insert the id of the match you want to end: "))-1
        input_score = float(input("Please enter the score of player1 (0=lost, 1=winner, 0.5=stalemate):  "))
        
        input_score_player1=input_score

        if input_score_player1== 1 :  
            input_score_player2=0  
            print('The winner is player1')
                
        elif input_score_player1 == 0 : 
            input_score_player2=1
            print("The winner is player2")
                
        elif input_score_player1 == 0.5: 
            input_score_player2=0.5
            print("stalemate")
        else:
            print("ERROR!")
        
        print("Match ended")
        return input_score_player1,input_score_player2, input_ID

       
    @staticmethod
    def resume_tournament_view():
        input_score = input("Please enter the score of the completed match :  ")
        print("tournament ended")
        return input_score   
    @staticmethod
    def resume_round_view():
        date=datetime.now()
        resp = input("Are you sure do you want to finish the round?: y/n ")
        if resp=='y':
            print("round ended")
            return str(date.strftime('%H:%M:%S,%d/%m/%Y'))   
    
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
        print("Player added to the tournament\n ")
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
            
            
            
        
            
    

