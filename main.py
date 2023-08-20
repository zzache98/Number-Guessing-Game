from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def compare(user_guess, chosen_number, turns):
  if user_guess < chosen_number:
    print("Too low.") 
    return turns - 1
  elif user_guess > chosen_number:
    print("Too high.") 
    return turns - 1
  elif user_guess == chosen_number:
    print(f"Correct! The number was {chosen_number}. You win.") 

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    return EASY_LEVEL_TURNS
  elif difficulty == "hard":
    return HARD_LEVEL_TURNS
  
def game(): 
  print(logo) 
  print("Welcome to the number guessing game!")
  print("Im thinking of a number between 1 and 100")    
  chosen_number = randint(1,100)
  
  turns = set_difficulty()
  user_guess = 0
  while user_guess != chosen_number:
    print(f"You have {turns} attempts remaining to guess")
    user_guess = int(input("Make a guess: "))
    turns = compare(user_guess, chosen_number, turns)
    
    if turns == 0:
      print("You lost")
      return
    elif user_guess != chosen_number:
      print("Guess again.")
    
game()