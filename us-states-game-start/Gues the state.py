import turtle #, Screen

import pandas 

screen = turtle.Screen()
screen.title("U.S. STATE")

image = "/Users/mohit/Desktop/us-states-game-start/blank_states_img.gif"
screen.addshape(image) 
turtle.shape(image)

data = pandas.read_csv("/Users/mohit/Desktop/us-states-game-start/50_states.csv") 
all_states = data.state.to_list() 
guessed_state = []

while len(guessed_state)< 50:

    ans= screen.textinput(title= f"{len(guessed_state)}/ 50 states Correct ", prompt ="Whats ther another state's name ").title()
    
    print(ans) 
    
    
    if ans == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state ]
        
        
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_toL_learn.csv") 
        break
            
    print(missing_states)
    
    if ans in all_states:
        guessed_state.append(ans)  
        
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans]
        t.goto(int(state_data.x) , int(state_data.y)) 
        t.write(ans) 
        
    
    
