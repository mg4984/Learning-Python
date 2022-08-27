import random
Rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
a= [Rock, Paper, Scissors]
user=eval(input("CHOOSE ROCK,PAPER,SCISSORS by typing 0,1,2 \n"))
print (a[user])
computer=random.randint(0,2)
print("COMPUTER CHOOSE")
print(a[computer])
if(user>=3 or user<0):
    print("YOU TYPED WRONG YOU LOSE")
elif(user==0 and computer==2):
    print("YOU WIN")
elif computer > user:
    print("YOU LOSE")
elif(computer==0 and user==2):
    print("YOU LOSE")
elif(user > computer):
    print("YOU WON")
elif (computer==user):
    print("ITS A DRAW")