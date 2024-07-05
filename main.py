
import os
from art import logo
import random
clear=lambda: os.system('cls')


#1: Create a deal_card() function
def deal_card():
    """ 
    - Returns a Random card 
    """
    deck=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)


#3: Create Calculate_Score() function
def calculate_score(list_of_cards):
    """
    - returns the sum of provided list of cards
    """
    #4: Check if blacjack
    if len(list_of_cards)==2 and {11,10}.issubset(list_of_cards):
        return 0
    
    #5: Check for an ace if the score is over 21
    if sum(list_of_cards) > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    
    return sum(list_of_cards)


#11: Create a compare() function and pass in the user_score and computer_score
def compare(user_score, computer_score):
    """
    - Compares the scores and return the results accordingly.
    """
    if computer_score==user_score:
        return "It's a draw. 🤝"
    elif computer_score==0:
        return "Loose, Opponent has a Blackjack." 
    elif user_score==0:
        return "Win with a Blackjack."

    elif user_score > 21:
        return "You went over. You lose. 😭"

    elif computer_score>21:
        return "Opponent went over. You win!!! 😁"
    
    elif user_score>computer_score:
        return "You win!!! 😁"

    else:
        return "You Lose!!! 😭"


def blackjack():
    #6: Call calculate_score() function
    user_score=calculate_score(list_of_cards=user_card)
    computer_score=calculate_score(list_of_cards=computer_card)

    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer's first card: {computer_card[0]}")

    #7: Calling the calculate_score() function
    if user_score ==0 or computer_score ==0 or user_score>21:
        return {
            "result":compare(user_score, computer_score),
            "computer_score": computer_score,
            "user_score": user_score
        }

    #8: If game not ended, ask the user if they want to draw another card.
    ask_user= input("\nType 'y' to get another card, type 'n' to pass: ").lower()

    if ask_user == 'y':
        #9: Draw new card and check the new score
        draw_Card=deal_card()
        user_card.append(draw_Card)
        return blackjack()
        
    else:
        #10: Now let the computer play.
        while computer_score<17:
            draw_Card=deal_card()
            computer_card.append(draw_Card)
            computer_score=calculate_score(list_of_cards=computer_card)
        
        return {
            "result":compare(user_score, computer_score),
            "computer_score": computer_score,
            "user_score": user_score
        }


#12: Asking user if they want to restart the game. 
new_game=True
while new_game==True:
    decision=input("\nDo you want to play the game of Blackjack? Type 'y' or 'n': ").lower()

    if decision =='y':
        clear()
        print(logo)
        #2: Deal the user and computer 2 cards each using deal_card()
        user_card=[]
        computer_card=[]

        for _ in range(2):
            user_card.append(deal_card())
            computer_card.append(deal_card())
        
        data=blackjack()
        
        print(f"\nYour final hand: {user_card}, final score: {data['user_score']}")
        print(f"Computer's final hand: {computer_card}, final score: {data['computer_score']}")
        print(data['result'])

    else:
        clear()
        new_game=False

