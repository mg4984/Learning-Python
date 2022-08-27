import random


def deal_card():
   
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card 

def calculate_scores(cards):
   
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare(user_score, computer_score):
    if user_score== computer_score:
        return "DRAW 🥲"
    
    elif computer_score==0:
        return "SHIT! OPPONENT HAS WON🤯"
    elif user_score==0:
        return "WUHU!!! YOU WON😭"
    elif user_score>21:
        return "YOU LOSE"
    elif computer_score>21:
        return "YOU WON"
    elif user_score>computer_score:
        return "you won"
    else:
        return "YOU LOSE"

    
user_card=[]
computer_card=[]
is_game_over = False
for _ in range(2):
    user_card.append(deal_card()) 
    computer_card.append(deal_card())

while not is_game_over : 
    user_score= calculate_scores(user_card)
    computer_score= calculate_scores(computer_card) 
    print("YOUR cards :",user_card , "CURRENT SCORE: ",user_score,)
    print("COMPUTER'S FIRST CARD: ",computer_card[0])

    if user_score==0 or computer_score==0 or user_score>21:
     is_game_over= True 
    else:
        user_should_deal=input("TYPE 'y' to get another card, type 'n' to pass: " ) 
        if user_should_deal=="y":
            user_card.append(deal_card())
            user_score=calculate_scores(user_card)
            print("YOUR cards :",user_card , "CURRENT SCORE: ",user_score,)
        else:
            is_game_over= True
while computer_score!=0 and computer_score<17:
    computer_card.append(deal_card())
    computer_score= calculate_scores(computer_card )

print(compare(user_score, computer_score)) 
