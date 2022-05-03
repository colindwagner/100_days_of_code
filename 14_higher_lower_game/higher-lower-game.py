#who has more followers on instagram
#higher or lower

from game_data import data
import random
from art import logo, vs

def get_random_person():
    return random.choice(data)

def compare_followers(a,b):
    if a['follower_count'] > b['follower_count']:
        return a
    else:
        return b

def assign_pick(pick, a, b):
    if pick == 'a':
        return a
    else:
        return b

def determine_winner(pick, winner):
    if pick['name'] == winner['name']:
        return True
    else:
        return False

def higher_or_lower_game():
    score = 0
    continue_game = True
    person_a = get_random_person()
    person_b = get_random_person()

    while continue_game:
        person_b = get_random_person()
        print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")

        print(vs)
        person_b = get_random_person()
        print(f"{person_b['name']}, a {person_b['description']}, from {person_b['country']}")


        user_pick = input("Who has more followers? Yup 'A' or 'B': ").lower()
        winner = compare_followers(person_a,person_b)
        user_pick = assign_pick(user_pick, person_a, person_b)

        if determine_winner(pick=user_pick, winner=winner):
            score += 1
            person_a = winner
            print(f"You Win! Score: {score}")
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            continue_game = False


print(logo)
higher_or_lower_game()