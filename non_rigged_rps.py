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

ask_user = input("what would you like to choose:\n0 for rock \n1 for paper \n2 for scissors , then press enter\n")
ask_user_int = int(ask_user)
if ask_user_int == 0:
  print("You chose:\n" + rock)
elif ask_user_int == 1:
  print("You chose:\n" + paper)
elif ask_user_int == 2:
  print("You chose:\n" + scissors)



rndm_val = random.randint(0,2)
if rndm_val == 0:
  print("Computer chose:\n" + rock)
elif rndm_val == 1:
  print("Computer chose:\n" + paper)
if rndm_val == 2:
  print("Computer chose:\n" + scissors)

# rock > scissors
# paper > rock
# scissors > rock

if rndm_val == ask_user_int:
  print("It is a tie!")
elif ask_user_int == 0 and rndm_val == 1:
  print("You lose,paper covers rock!")
elif ask_user_int == 0 and rndm_val == 2:
  print("You win,rock crushes paper!")
elif ask_user_int == 1 and rndm_val == 2:
  print("You lose, scissors cut paper!")
elif ask_user_int == 1 and rndm_val == 0:
  print("You win, Paper covers rock!")
elif ask_user_int == 2 and rndm_val == 0:
  print("You lose, rock crushes scissors")
elif ask_user_int == 2 and rndm_val == 1:
  print("You win, Scissors cut paper!")
else:
  print("chose a correct input!")


#not rigged
