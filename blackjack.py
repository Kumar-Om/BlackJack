import random as r
from replit import clear
import emoji as e

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]


def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    """ returns random card"""
    a=r.choice(cards)
    return a


def cal_score(cards):
    """inputs the list and return the sum """
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,comp_score):
    """compare the value nd return"""
    if user_score==comp_score:
        return "Draw!",e.emojize(":upside-down_face:")
    elif comp_score==0:
        return "You Lose",e.emojize(":crying_face:")
    elif user_score==0:
        return "You Win!",e.emojize(":smiling_face:")
    elif user_score>21:
        return"You Lose",e.emojize(":crying_face:")
    elif comp_score>21:
        return "You Win!",e.emojize(":smiling_face:")
    else:
        if user_score>comp_score:
            return "You Win!",e.emojize(":smiling_face:")
        else:
            return "You Lose",e.emojize(":crying_face:")
def game():
   
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
                   

                                      
     
    print(logo)
    user_cards=[]
    comp_cards=[]
    gameover=False
    for i in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    # print(user_cards)
    # print(comp_cards)
    while gameover!=True:
        user_score=cal_score(user_cards)
        comp_score=cal_score(comp_cards)
        print(f"your cards:{user_cards},Your score:{user_score}")
        print("computer 1st card:",comp_cards[0])
        if user_score==0 or comp_score==0 or user_score>21:
            gameover=True
        else:
            c=input("If you want to draw new card, y or n:")

            if c=="y":
                user_cards.append(deal_cards())
            else:
                gameover=True

    while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_cards())
        comp_score=cal_score(comp_cards)
    print(f"your final hand{user_cards},your final score:{user_score}")
    print(f"computer final hand:{comp_cards},computer final score:{comp_score}")
    print(compare(user_score,comp_score))

while input("Do you want play BlackJack, y or n:")=="y":
    clear()
    game()

