from datetime import datetime
import json


class MainView:

    @classmethod   
    def showMenu (cls) :
        print("\n__________________________________")
        print("             WELCOME")
        print("__________________________________\n")
        print('Please select a action:\n')
        print('1: Create a tournament')
        print('2: Create players')
        print('3: Get_player to tournament')
        print('4: Reports')
        print('5: Default')
        print('6: Resume tournament')
        print('7: Generate JSON file')
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
    def resume_match_view(match, players_list):
        id_player = match.player1-1 #
        id_player2 = match.player2-1
        print("\nMatch",match)

        message = f"Please enter the score of {players_list[id_player].first_name}"
        input_score = float(input(message + " (0=lost, 1=winner, 0.5=stalemate) of match #  "))
        
        input_score_player1=input_score

        if input_score_player1== 1.0 :  
            input_score_player2=0.0  
            print('The winner is player1 ',players_list[id_player].first_name)
                
        elif input_score_player1 == 0.0 : 
            input_score_player2=1.0
            print("The winner is player2 ",players_list[id_player2].first_name)
                
        elif input_score_player1 == 0.5: 
            input_score_player2=0.5
            print("stalemate")
        else:
            print("ERROR!")
        
        print("\nMatch ended")
        return input_score_player1,input_score_player2,

       
   
    @staticmethod
    def resume_round_view():
        date=datetime.now()
        resp = input("To end the round, insert 'y': ")
        if resp=='y':
            print("Round ended")
            return str(date.strftime('%H:%M:%S,%d/%m/%Y'))   
    
    @classmethod
    
    def newplayer_view(cls):
        input_national_ID = input("Please enter your national ID: ")
        input_first_name = input("Insert first_name: ")
        input_last_name = input("Insert the last name of player:  ")
        input_date_of_birth = input("Insert the date_of_birth: ")
        input_gender = input("Insert gender of player: ")
        
        return {
            'national_ID': input_national_ID,
            'first_name': input_first_name, 
            'last_name': input_last_name, 
            'date_of_birth': input_date_of_birth, 
            'gender': input_gender
            }
        

    def get_player():
        input_player_id = int(input("Insert the id of player: "))  
        print("Player added to the tournament\n ")
        return input_player_id -1
        
    @staticmethod  #metodo que no requiere de una instancia de la clase para ser llamado  
    def show_players_list(players_list):
    
        players_list=sorted(players_list, key=lambda x: x.first_name)# para ordenar por orden alphabetico del nombre
        for p in range(0, len(players_list)):
            print(f" {players_list[p]}")
            
    
    
    
    @staticmethod    
    def show_tournament_list(tournament_list):
        
        tournament_list =sorted(tournament_list, key=lambda x: x.name)
        for t in range(0, len(tournament_list)):
            print(f"{tournament_list[t]}")
            
            
    def generateJson(tournament_list, players_list,rounds_list, match_list,winner):
        players_data=[]
        tournaments_data=[]
        rounds_data=[]
        match_data=[]

        for p in range(0, len(players_list)):
            
            players_dict={
            "Players :"+
            "ID": players_list[p].ID,
            "first_name": players_list[p].first_name,
            "last_name": players_list[p].last_name, 
            "date_of_birth": players_list[p]. date_of_birth,
            "gender": players_list[p].gender
            }
            players_data.append(players_dict)

        for m in range(0, len(match_list)):
            
            match_dict={
            "ID": match_list[m].ID,
            "scorePlayer1": match_list[m].scorePlayer1,
            "scorePlayer2": match_list[m].scorePlayer2, 
            "player1": match_list[m]. player1,
            "player2": match_list[m].player2,
            "color_player1": match_list[m].color_player1,
            "color_player2": match_list[m].color_player2
            }
            match_data.append(match_dict)
        
        for r in range(0, len(rounds_list)):
            rounds_dict={
            "name": rounds_list[r].name,
            "round_number": rounds_list[r].round_number,
            "start_time": rounds_list[r].start_time, 
            "end_time": rounds_list[r]. end_time,
            "matches": match_data
            }
            rounds_data.append(rounds_dict)

        
        for t in range(0, len(tournament_list)):
            
            tournament_dict = {
                "Tournament : " + 'id': tournament_list[t].ID,
                'name': tournament_list[t].name,
                'location': tournament_list[t].location,
                'number_rounds': tournament_list[t].number_rounds,
                'description': tournament_list[t].description,
                'list of players': players_data,
                'list of rounds': rounds_data,
                'The winner is': winner
                                 }

            # Add the dictionnay to the data list of tournaments
            tournaments_data.append(tournament_dict)

            # Open a file in a write mode   
            with open("tournament.json", 'w') as file:
                # Write the data list of tournaments in JSON format
                json.dump(tournaments_data, file, indent=4)     