#Write your code below this row 👇

#FizzBuzz Game

list_of_numbers = range(1,101)

for number in list_of_numbers:
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 5 == 0:
    print("fizz")
  elif number % 3 == 0:
    print("Buzz")
  else:
    print(number)

#Game done