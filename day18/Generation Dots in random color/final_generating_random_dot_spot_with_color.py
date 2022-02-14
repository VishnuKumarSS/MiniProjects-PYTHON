import numbers
import turtle as t
import random

def random_color(): # this funcion is the define the rgb color.
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b) # tuple
    return colour


jilly = t.Turtle()
t.colormode(255)
jilly.speed(15)
jilly.penup()
jilly.hideturtle()

# creating 10 colours
how_many_colours = 10
rgb_list = []
for i in range(how_many_colours):
    rgb_list.append(random_color())
# print(rgb_colours)

jilly.setheading(225)
jilly.forward(250)
jilly.setheading(0)

number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    jilly.dot(20, random.choice(rgb_list))
    jilly.forward(50)

    if dot_count % 10 == 0:
        jilly.setheading(90)
        jilly.forward(50)
        jilly.setheading(180)
        jilly.forward(500)
        jilly.setheading(0)


screen = t.Screen()
screen = t.exitonclick()