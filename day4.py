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

user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
options = [rock, paper, scissors]
user_input=options[user_choice]
print(f"you chose: {user_input}")

computer_input=random.choice(options)
print(f"computer chose: {computer_input}")

if user_input == computer_input:
    print("It's a tie!")
elif user_input == rock and computer_input == paper:
    print("You win!")
elif user_input == rock and computer_input == scissors:
    print("You win!")
elif user_input == paper and computer_input == rock:
    print("You win!")
else:
    print("You lose!")
