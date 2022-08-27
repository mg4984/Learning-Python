import random
from turtle import Turtle,Screen
is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="ENTER YOUR BET",prompt="WHICH TURTLE WILL WIN THE RACE?")
colors= ["purple","green","blue","yellow","red"]
y_positions= [-90,-40,10,60,110]
all_turtles=[]

for turtle_index in range(0,5):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True
    
while is_race_on:
    for turtle in all_turtles:
       if turtle.xcor() >230:
           is_race_on=False
           winning_color=turtle.pencolor()
           
           
           if winning_color==user_bet:
               print("YOU HAVE WON",winning_color)
           else:
               print("better luck next time ")
            
           
           
           
       random_distance=random.randint(0,10)
       turtle.forward(random_distance)

screen.exitonclick()
