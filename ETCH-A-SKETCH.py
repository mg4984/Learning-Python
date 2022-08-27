from turtle import Turtle, Screen

tim = Turtle()
screen=Screen()

def move_forward():
    tim.forward(100)
    
def move_backward():
    tim.backward(100)
    
    
def turn_left():
    #new_heading= tim.heading()+100
    #tim.setheading(new_heading)
    tim.left(10)
    
    
def turn_right():
    tim.right(80)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")




screen.exitonclick()
