# https://www.sporcle.com/games/g/states

import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game')

#turtle only works with gifs
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

#this is how we could get state coordinates if not in csv
# def get_mouse_click_coord(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coord)

#get data from csv
data = pandas.read_csv('50_states.csv')
state_list = data.state.to_list()
user_answers = []

game_is_on = True

while game_is_on and len(user_answers)<50:

    #get user answer
    answer_state = screen.textinput(title=f"{len(user_answers)}/50 Guess the state", prompt="What's another state's name?\n (or 'exit' to give up)").title()

    if answer_state == 'Exit':
        game_is_on = False

    #good guess but not yet guessed
    if answer_state in state_list and answer_state not in user_answers:
        user_answers.append(answer_state)
        x_coord = int(data[data.state == answer_state].x)
        y_coord = int(data[data.state == answer_state].y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_coord,y_coord)
        t.write(answer_state)
        print(user_answers)

    screen.tracer(1) # focus textinput

#generate states_to_learn.csv
# states_to_learn = []
# for item in state_list:
#     if item not in user_answers:
#         states_to_learn.append(item)

states_to_learn = [state for state in state_list if state not in user_answers]

df = pandas.DataFrame(states_to_learn)
df.to_csv('states_to_learn.csv')





# turtle.mainloop() #keep screen open after click

