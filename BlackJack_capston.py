# Blackjack Capston Project
from dataclasses import replace
import random
from turtle import clear
 
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
# A function which returns a random card.
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

# A function which return the users and computer's score.
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:  #checking BlackJack in our game.
        return 0
    if 11 in cards and sum(cards)>21:
        cards.replace(11,1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Its draw!"
    elif computer_score==0:
        return "Lose, Opponent has Blackjack."
    elif user_score==0:
        return "You win with a Blackjack. "
    elif user_score>21:
        return "You lose. You went over the limit 21."
    elif computer_score>21:
        return "You win. Computer went over the limit 21."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "Computer win!"
def play_game():
    user_cards=[]
    computer_cards=[]
    for _ in range(2):      # for taking two cards for user and for computer from cards using deal_card()
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    is_game_over=False # To confirm that game is still continue or ended.

    while not is_game_over:  # score need to be checked with new card drawn.(Its for user.)


    # calling calculate_score() function to return the score of both user and computer
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)   
        print(f" Your cards:{user_cards}, current score:{user_score}")
        print(f" computer's first card: {computer_cards[0]}")

        if user_score ==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else: 
            draw=input("You want to draw another card, Type 'y'. \n")
            if draw=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True

        
        
    while computer_score>0 and computer_score<17: # its for computer to draw the cards until the score become less than 17
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"  Your final cards:{user_cards}, final score: {user_score}")
    print(f"  Computer's final cards:{computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

#If user want to restart the game
while input("Do you want to play the game again? Type 'y' for yess and 'n' for no: \n"):
    clear()
    print(logo)
    play_game()