import turtle
import pandas
screen = turtle.Screen()
image = "indianmap.gif"
screen.title("Indian States Quiz Game")
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("indian_states.csv")
state = data.state.to_list()
guessed_state = []
state_to_learn =[]
while len(guessed_state)<30:
    user_input = screen.textinput(title=f"Quiz Time {len(guessed_state)}/28", prompt="Enter An Indian State").title()
    if user_input=="Exit":
        for s in state:
            if s not in guessed_state:
                state_to_learn.append(s)
        new_data = pandas.DataFrame(state_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if user_input in state:
        guessed_state.append(user_input)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_input]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(user_input,align="center",font=("Arial",10,"bold"))
        
        
