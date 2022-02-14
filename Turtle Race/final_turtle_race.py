from turtle import Turtle, Screen, xcor
import random

colours = ["violet","blue","green","yellow","orange","red"]

start_race = False
screen = Screen()
screen.setup(width= 600, height=400)
user_input = screen.textinput(title="Make Your Choice: ", prompt="Which Turtle will win the race?")

y_positions = [-75,-45,-15,15,45,75]

all_turtles = []
for i in range(len(colours)):
    turtle = Turtle(shape="turtle")
    turtle.color(colours[i])        
    turtle.penup()
    turtle.goto(x=-270,y=y_positions[i]) # think like graph points.
    all_turtles.append(turtle)

# just to know all the turtle colours
# for turtle in all_turtles:
#     print(turtle.pencolor())

if user_input: # if user input is given, the racce will start
    start_race = True

while start_race:
    for turtle in all_turtles:
        if turtle.xcor() > 280: # if x point reaches the 280 width from the middle of the graph, the race will end.
            start_race = False
            winner = turtle.pencolor()
            if winner == user_input:
                print(f"You WON! The winner is {winner} Turtle.")
            else:
                print(f"You LOSE! The winner is {winner} Turtle.")

        movement_distance = random.randint(0,10)
        turtle.forward(movement_distance)

screen.exitonclick()
