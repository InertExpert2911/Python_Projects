# A program that user has to make choices to get the treasure.

# ASCII art
print("""
 _____                                   _   _             _   
|_   _|                                 | | | |           | |  
  | |_ __ ___  __ _ ___ _   _ _ __ ___  | |_| |_   _ _ __ | |_ 
  | | '__/ _ \/ _` / __| | | | '__/ _ \ |  _  | | | | '_ \| __|
  | | | |  __/ (_| \__ \ |_| | | |  __/ | | | | |_| | | | | |_ 
  \_/_|  \___|\__,_|___/\__,_|_|  \___| \_| |_/\__,_|_| |_|\__|

""")

# Welcome text
print("Welcome to the treasure hunt!!")

# User input
user_choice_0 = input("Your mission is to find the treasure and give it to the government, should you choose to accept it? Type Y or N: ").lower()

if user_choice_0 == 'y':
    
    print("Let's start the mission, we have no time to waste.")
    
    user_choice_1 = input("You are at a cross road. Which direction do you want to go? Type 'left' or 'right' \n").lower()
    
    # print(user_choice_1)
    
    if user_choice_1 == 'left':
        
        user_choice_2 = input("You see a river stream, do you want wait for the boat or swim to the other side? Type 'wait' or 'swim' \n").lower()
        
        if user_choice_2 == 'wait':
            
            user_choice_3 = input("You safely reach to the other side of the river and you see three doors in-front of you a 'red', 'green' and 'yellow' coloured. Choose a color: \n").lower()
            
            # Elif conditionals, catching multiple cases
            if user_choice_3 == 'yellow':
                
                print("You found the treasure, after giving it to the government. They awarded the most prestigious award and you retired.")
            
            elif user_choice_3 == 'red':
                print("As you enter the room, you are surrounded by enemy military. GAME OVER!!")
                
            elif user_choice_3 == 'green':
                print("A bear killed you. GAME OVER!!")
                
            else:
                print("You chose a door that doesn't exist. GAME OVER!!")
                
        else:
            print("River is filled with alligators. GAME OVER!!")
    
    else:
        print("The path is filled with mines and you stepped on one of the mine. GAME OVER!!")

else:
    print("Your choice is noted, and the mission is given to a different agent.")
