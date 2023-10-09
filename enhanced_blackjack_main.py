import random
from replit import clear
from art import logo

# Constants
SUITS = ["♥", "♦", "♠", "♣"]

# Deal a card: returns a tuple with card value and suit
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    random_suit = random.choice(SUITS)
    return (random_card, random_suit)

# Calculate score: return the score of a hand, handling aces properly
def calculate_score(cards):
    score = sum(card[0] for card in cards)
    contains_ace = any(card[0] == 11 for card in cards)
    
    # Handle Ace (make it 1 if score would otherwise bust)
    if score > 21 and contains_ace:
        score -= 10
    
    return score

# Display cards in a more human-friendly way
def display_cards(cards):
    return " ".join([f"{card[0]}{card[1]}" for card in cards])

# Compare scores and determine winner
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😭"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😤"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Initial dealing for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    # Game loop
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {display_cards(user_cards)}, current score: {user_score}")
        print(f"Computer's first card: {display_cards(computer_cards[:1])}")

        # Check for Blackjack or bust for user/computer to end game
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    # Once user is done, let computer draw cards until it reaches at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {display_cards(user_cards)}, final score: {user_score}")
    print(f"    Computer's final hand: {display_cards(computer_cards)}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Game entrance: loop that keeps the game going as long as user wants to play
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
