# Day 2

bill = 200

def tip_calculator(bill, tip_percentage, number_of_payments):
  tip = bill * tip_percentage
  total_cost = bill + tip
  each_payment = total_cost/number_of_payments
  print(each_payment)

tip_calculator(bill, .15, 5)

def even_or_odd(number):
  answer = number / 2
  if number % 2 != 0:
    return print(f"This number is odd. {number} / 2 = {answer}, and {answer} is not a whole number.")
  else:
    return print(f"This number is even. {number} / 2 = {answer}, and {answer} is a whole number.")
  
even_or_odd(7)

import random

options = ["heads", "tails"]

def coin_toss(set):
  choice = random.choice(set)
  if choice == "heads":
    print("heads")
    yes_or_no = input("Would you like to play again?")
    if yes_or_no == "y":
      coin_toss(options)
    else:
      return print("Thanks for playing.")
  else:
    print("tails")
    yes_or_no = input("Would you like to play again? (y or n)")
    if yes_or_no == "y":
      return coin_toss(options)
    else:
      return print("Thanks for playing.")


  
coin_toss(options)