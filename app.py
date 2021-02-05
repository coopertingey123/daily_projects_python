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


heights = [100, 122, 111, 122, 121, 106]

def number_of_heights(heights):
  i = 0
  height_sum = 0
  for height in heights:
    i = i + 1
    height_sum = height + height_sum
  return print(int(height_sum/i))

number_of_heights(heights)

scores = [100, 122, 111, 122, 121, 106, 134]

def highest_score(list_of_scores):
  highest_score = list_of_scores[0]
  for score in list_of_scores:
    if score > highest_score:
      highest_score = score
  return print(highest_score)

highest_score(scores)

def fizzbuzz(max_number):
  list_of_nums = range(0, max_number)
  for num in list_of_nums:
    if num % 3 == 0 and num % 5 == 0:
      print("fizzbuzz")
    elif num % 5 == 0:
      print("buzz")
    elif num % 3 == 0:
      print("fizz")
    elif num != 0:
      print(num)
      
fizzbuzz(100)