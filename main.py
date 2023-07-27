import random
from replit import clear
from art import logo

def deal_card():
  """Defines a function that can returns a random number upon calling."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card


def calculate_score(card):
  """Takes the elements of a list and returns the sum/score of the card that has been put into the argument called 'card'"""
  if 11 in card and 10 in card and len(card) == "2":
    """Returns 0 if total sum of 2 cards is 21"""
    return 0

  if 11 in card and sum(card) > 21:
    """Changes ace of 11 to 1, if the sum of the cards exceeds 21, if the ace card exists"""
    card.remove(11)
    card.append(1)

  return sum(card)

def compare(user_score, computer_score):
  if computer_score == user_score:
    return "You've drawn."
  elif computer_score == 0:
    return "You lose, computer has a blackjack."
  elif user_score == 0:
    return "You win, you have a blackjack."
  elif computer_score > 21:
    return "You win, computer is busted."
  elif user_score > 21:
    return "You lose, you are busted."
  elif computer_score > user_score:
    return "You lose."
  else:
    return "You win."

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  game_condition = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  
  while not game_condition:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_condition = True
    else:
      next_card = input("Type 'y' to take another card, type 'n' to pass: ")
      if next_card == "y":
        user_cards.append(deal_card())
      else:
        game_condition = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"    Your final hand: {user_cards}, final score: {user_score}")
  print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
