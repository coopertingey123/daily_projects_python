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

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def random_letter(number_of_letters):
  i = 0
  password_letters = []
  while i < number_of_letters:
    i = i + 1
    password_letters.append(random.choice(letters))
  return password_letters

def random_number(number_of_numbers):
  i = 0
  password_numbers = []
  while i < number_of_numbers:
    i = i + 1
    password_numbers.append(random.choice(numbers))
  return password_numbers

def random_symbol(number_of_symbols):
  i = 0
  password_symbols = []
  while i < number_of_symbols:
    i = i + 1
    password_symbols.append(random.choice(symbols))
  return password_symbols

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters = random_letter(nr_letters)
symbols = random_symbol(nr_symbols)
numbers = random_number(nr_numbers)
password = (letters + symbols + numbers)
new_password = ''.join(password)
print(f'Your password is {new_password}.')

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    move()

while at_goal() != True:
    if front_is_clear() ==True:
        move()
    elif right_is_clear() ==True:
        turn_right()
    elif wall_on_right() ==True:
        turn_left()
        if front_is_clear() ==True:
            move()


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]

import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

def return_word(list_of_words):
  end_game = False
  random_word = random.choice(word_list) 
  print(random_word)
  display = []
  lives = 6
  word_length = len(random_word)
  print(logo)
  for _ in range(word_length):
      display += "_"
  while not end_game:
    letter_choice = input("Select a letter: ")
    for position in range(word_length):
      letter = random_word[position]
      if letter == letter_choice:
        display[position] = letter
        print(display)
        if "_" not in display:
          end_game = True
          print("You win.")
    if letter_choice not in random_word:
      lives = lives - 1
      print("That letter is not in the word. You lost a life. Try again!")
      if lives == 0:
        end_game = True
        print("You lose")
    print(stages[lives])


return_word(word_list)

def my_function(first_name, last_name):
  name = first_name + " " + last_name
  print(f"{first_name} {last_name} is your name.")
  print(f"Hello {name}.")

first_name = input("First name: ")
last_name = input("Last name: ")

my_function(first_name, last_name)
