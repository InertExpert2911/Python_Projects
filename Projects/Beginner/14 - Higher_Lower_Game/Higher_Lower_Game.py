from higher_lower_game_data import data
from higher_lower_game_logo import logo, vs

import random


def get_random_account():
    """Generates a random number and gets the index from the data list and gets all the values in the dictionary and returns all those values."""

    random_list_index = random.randint(0, len(data) - 1)
    user_account = data[random_list_index]
    
    user_name = user_account['name']
    user_description = user_account['description']
    user_country = user_account['country']
    follower_count = user_account['follower_count']
    
    return user_name, user_description, user_country, follower_count


account = get_random_account()
print(account)

print(f"Compare A: {account[0]}, a {account[1]}, from {account[2]}")

user_score = 0

user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

if user_input == 'a':
    if follower_count_1 > follower_count_2:
        user_score += 1
        print(f"You're right! Current score: {user_score}.")

    else:
        # TODO: print logo, clear screen, end game
        print(f"Sorry, you got it wrong. Final score {user_score}.")
elif user_input == 'b':
    if follower_count_2 > follower_count_1:
        user_score += 1
        print(f"You're right! Current score: {user_score}.")
    else:
        # TODO: print logo, clear screen, end game
        print(f"Sorry, you got it wrong. Final score {user_score}.")
