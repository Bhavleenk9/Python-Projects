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

import random
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n"))
if user_choice == 0: 
  print("User's choice :")
  print(rock)
if computer_choice == 0:
  print("Computer's choice :")
  print(rock)
if user_choice == 1: 
  print("User's choice :")
  print(paper)
if computer_choice == 1:
  print("Computer's choice :")
  print(paper)
if user_choice == 2:  
  print("User's choice :")
  print(scissors)
if computer_choice == 2:
  print("Computer's choice :")
  print(scissors)
if user_choice == computer_choice:
  print("Draw!")
elif user_choice == 0 and computer_choice == 1:
  print("you win!")
elif user_choice == 0 and computer_choice == 2:
  print("you lose!")
elif user_choice == 1 and computer_choice == 0:
  print("you win!")
elif user_choice == 1 and computer_choice == 2:
  print("you lose!")
elif user_choice == 2 and computer_choice == 0:
  print("you lose!")
elif user_choice == 2 and computer_choice == 1:
  print("you win!")
else:
  print("you typed an invalid number, you lose!")
