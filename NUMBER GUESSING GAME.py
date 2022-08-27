from random import randint

EASY_LEVEL_TURNS= 10
HARD_LEVEL_TURNS= 5

def check_answer(answer, guess,turns):
    if guess>answer:
        print("TOO HIGH!")
        return turns-1
    elif guess<answer:
        print("TOO LOW!")
        return turns-1
    else:
        print("YOU WON!!!",answer)

def check_difficulty():
    level=input("CHOOSE A DIFFICULTY: easy or hard: ")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        
def game():
    print("WELCOME! TO THE NUMBER GUESSING GAME")
    print("I AM THINKING OF A NUMBER BETWEEN 0 to 100 ")
    answer= randint(0,100)
    print("PSST,THE CORRECT ANSWER IS",answer)
    
    turns=check_difficulty()
   
    guess=0
    while guess!=answer:
        print("you have",turns,"attempts remainng to guess")
        guess=int(input("MAKE A GUESS: "))
        turns=check_answer(answer, guess,turns)
        if turns==0:
            print("YOU OUT")
            return

game() 