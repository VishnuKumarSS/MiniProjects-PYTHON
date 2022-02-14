from turtle import Turtle
import random
# creating the Food class inherit from the Turtle class
class Food(Turtle):    
    def __init__(self):
        super().__init__()
        # food shape
        self.shape("circle") # method shape inherited from the Turtle class.
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # default shape size is 20/20...we are changing the default shape size to 10/10
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # below code is to make the food location randomized.
        # remember that out width is 800, height is 600
        x_axis_random = random.randint(-360,360) # x-axis random value 
        y_axis_random = random.randint(-260,260) # y-axis random value.
        self.goto(x_axis_random,y_axis_random)
