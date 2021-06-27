#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

passwrd = ''

for characters in range(1, nr_letters + 1):
  passwrd += random.choice(letters)
   

for symbl in range(1, nr_symbols + 1):
  passwrd += random.choice(symbols)

for nums in range(1, nr_numbers + 1):
  passwrd += random.choice(numbers)

print(f"Your strong password is {passwrd}")

length = len(passwrd)

print(f"The length of your password is {length},characters")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_pass = ''
for characters in range(1, length):
  hard_pass += random.choice(passwrd)

length_2 = len(hard_pass)
print(f"Your super strong password is {hard_pass}")
print(f"The length of your password is {length_2},characters")



