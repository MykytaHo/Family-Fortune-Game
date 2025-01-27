import random # random Questions each time the game is played#

import time # Import time to add a small delay

def rules_of_the_game(): # Displaying the rules of the game by creating a function.#

    print ("Welcome to Family Fortune")

    print ("You will be asked a number of questions")

    print ("The frist person to buzz in(player 1 will hit enter, player 2 will hit spacebar) will go first")

    print ("If any of the team get the guess frist answer correct, they will continue with the game and, get the points")

    print ("If they guess 3 wrong answers, the other team go and get a chance to steal the pther teams points")

#rules of the game ends#

rules_of_the_game()



# Start the buzzer simulation

def wait_for_buzzer():

            print("Player 1, press Enter to buzz in...")

            print("Player 2, press 2 to buzz in...")

        # Loop until a valid buzzer input is given

            while True:
                player_input = input("Press 1 (Player 1) or 2 (Player 2) to buzz in: ")
                
                if player_input == '1': # If Player 1 presses Enter
                   
                    print("Player 1 buzzed in first!")
                    
                    return "Player 1"
                
                elif player_input == '2': # If Player 2 presses '2'
                    
                    print("Player 2 buzzed in first!")
                    
                    return "Player 2"
                
                else:
                    
                    print("Invalid input!")

def again():
            play_again = input("Press 'y' if you want to play again or 'n' if not ")
            
            if play_again == 'y': # If you want to paly again
               
                family_fortune_game()
            
            elif play_again == 'n': # If not
                
                print("Have a good day")
                
            
            else:
                
                print("I dont understand you")
                again()
                
                


# Display who goes first
def family_fortune_game():
        
            
        
        questions = {
            "Name a fruit that is often eaten for breakfast": ["banana", "apple", "orange", "strawberry", "grape"],
            "Name something people do before going to bed": ["brush teeth", "read", "watch TV", "set alarm"],
            "Name an animal that lives in the water": ["fish", "shark", "whale", "dolphin", "seal"]
        }
        rounds = 3
        scores = {"Player 1": 0, "Player 2": 0}        
        remaining_questions = list(questions.items())
        
        
        for _ in range(rounds):  # Play 3 rounds
            question, answers = random.choice(list(remaining_questions))
            print("\nQuestion:", question)
            
            
            first_player = wait_for_buzzer()
            attempts = 0
            while attempts < rounds:
                user_answer = input(f"{first_player}, your answer: ").strip().lower()
                if user_answer in [answer.lower() for answer in answers]:
                    print("Correct!")
                    scores[first_player] += 10
                    break
                else:
                    print("Wrong answer!")
                    attempts += 1
            
            if attempts == 3:
                print(f"3 wrong answers! The other player gets a chance to steal.")
                other_player = "Player 1" if first_player == "Player 2" else "Player 2"
                user_answer = input(f"{other_player}, your answer: ").strip().lower()
                if user_answer in [answer.lower() for answer in answers]:
                    print("Correct! Points stolen!")
                    scores[other_player] += 10
                else:
                    print("Wrong answer! No points awarded.")
        
            remaining_questions = [q for q in remaining_questions if q[0] != question]
        
        print("\nFinal Scores:")
        for player, score in scores.items():
            print(f"{player}: {score} points")
            
        
        again()
             
            
family_fortune_game()



