from higher_lower_game_data import data
from higher_lower_game_logo import logo, vs

import random

# print(logo)

# TODO-1: GET A RANDOM item from the dictionary


def get_random_account():
    """Generates a random number to fetch data from the data list and returns the user account details."""

    random_list_index = random.randint(0, len(data) - 1)
    user_account = data[random_list_index]
    return user_account


def extract_user_details(user_account):
    """Extract user details like name, description, country and follower count from a dictionary and returns"""

    user_name = user_account['name']
    description = user_account['description']
    user_country = user_account['country']
    follower_count = user_account['follower_count']

    
    # print(f"Compare A : {user_name}, a {description}, from {user_country}")


account_1 = get_random_account()
account_details_1 = extract_user_details(account_1)

print(account_details_1.user_name)


# account_2 = get_random_account()

# user_name_2 = account_2['name']
# description_2 = account_2['description']
# user_country_2 = account_2['country']
# follower_count_2 = account_2['follower_count']

# print(f"Against B : {user_name_2}, a {description_2}, from {user_country_2}")


# print(f"A - {follower_count_1}")
# print(f"B - {follower_count_2}")

# user_score = 0

# user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

# if user_input == 'a':
#     if follower_count_1 > follower_count_2:
#         user_score += 1
#         print(f"You're right! Current score: {user_score}.")

#     else:
#         # TODO: print logo, clear screen, end game
#         print(f"Sorry, you got it wrong. Final score {user_score}.")
# elif user_input == 'b':
#     if follower_count_2 > follower_count_1:
#         user_score += 1
#         print(f"You're right! Current score: {user_score}.")
#     else:
#         # TODO: print logo, clear screen, end game
#         print(f"Sorry, you got it wrong. Final score {user_score}.")
