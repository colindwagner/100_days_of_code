import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_input = random.randint(0,2)

list_of_options = [rock, paper, scissors]

print(list_of_options[player_input] + "\n" + list_of_options[computer_input])

if player_input == computer_input:
    print("It's a Draw")
elif player_input == 0 and computer_input == 1:
    print("You lose")
elif player_input == 1 and computer_input == 2:
    print("You lose")
elif player_input == 2 and computer_input == 0:
    print("You lose")
else:
    print("You win")