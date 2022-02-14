# creating class for creating the snake and moving the snake
# controling key press for the snake.

from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40,0)] # list of position values using tuples.
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = [] # body of the snake is stored as the squares in this list.
        self.create_snake()
        self.head = self.segments[0] # making the first segment of the snake body as head.

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self,pos):
        new_segment = Turtle(shape="square")
        new_segment.color("black")
        new_segment.penup() # to not to make the line   
        new_segment.goto(pos) # here the values of x and y inside the goto function set by looping through the positions list that we have created.
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position()) # to extend the snake, we have to add the new segment to the last segment of the list, so we are using -1

    def snake_move(self):
        for seg_num in range(len(self.segments) - 1 , 0 ,-1):  # range(start = len(segments)-1, stop = 0, step = -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE) # move forward by 20.
        # if we don't create a head attribute inside the __init__ function the above line will show error. we have to use self.segments[0] instead of self.head
    

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


