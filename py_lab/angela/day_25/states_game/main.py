import pandas
import turtle

screen=turtle.Screen()
screen.title("The states game")
image="blank_states_img.gif"
screen.addshape(image)



background=turtle.Turtle()
background.shape(image)


data=pandas.read_csv("50_states.csv")

your_state=[]

score=0

while True:
    
    user_input=screen.textinput(title=f"Score : {score}/50",prompt="Guess a state!")

    if type(user_input)==str:
        user_input=user_input.title()

    user_state=data[data.state==user_input]
    
    if user_state.state.to_list():
        your_state.append(user_input)
        state=user_state.state.to_list()[0]
        x=user_state.x.item()
        y=user_state.y.item()
        tim=turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(x,y)
        tim.write(state)
        score+=1

    if user_input==None:
        break



screen.mainloop()

you_should_study=[ name for name in data.state.to_list() if not name in your_state ]


data_dict={ "states": you_should_study}

new_data=pandas.DataFrame(data_dict)
new_data.to_csv("You should study this.csv")


