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

ask_user = input("what would you like to choose:\nr for rock \np for paper \ns for scissors , then press enter\n")

# rps_list = ["rock", "paper", "scissors"]

if ask_user == 'r':
  print(paper)
  print("I win, paper covers rock!")
elif ask_user == 'p':
  print(scissors)
  print("I win, scissors cut your paper!")
else:
  print(rock)
  print("I win, rock crushes your scissors!")