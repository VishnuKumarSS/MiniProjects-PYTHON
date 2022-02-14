from turtle import Screen
from snake import Snake
import time
from food_of_snake import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
# the screen height is 800 width, 600 height
# here height = y = 300,-300 ----- width = x=400,-400
screen.title("Snake Game - Vishnu")
screen.bgcolor("white") # setting background color as black.
screen.tracer(0) # it will stop the screen, and do not refresh until the update method is called.


snake = Snake() # creating object for the Snake class
food = Food() # creating object for the Food class
scoreboard = Scoreboard() # creating object for the Scoreboard class

# controling the snake with the up, down, right, left keys.
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_going = True
while game_is_going:
    screen.update() # here only the screen gets updated after tracer is called. The above code doesn't do anything until this update is called. (i.e) doesn't show anything on the screen until this method is called.
    time.sleep(0.1) # this adds 0.1 second delay to each segment moves.
    snake.snake_move()

    # detecting collision with food 
    if snake.head.distance(food) < 15: # remember that the pixel of the food is 10/10 (i.e) x axis - 10, y axis - 10. 
        food.refresh() # here refresh is the method in the Food class.
        snake.extend_snake() # extend_snake method in the Snake class
        scoreboard.increasing_score() 

    # detecting collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 280 or snake.head.ycor() < -280: 
        game_is_going = False
        scoreboard.game_over() 
        
    # detecting collision with tail of the snake.
    for segment in snake.segments[1:]:  ## detecting the snake collision expect the snake head (i.e) head is the first part of the list (i.e) 0
        if snake.head.distance(segment) < 10: 
            game_is_going = False
            scoreboard.game_over()



screen.exitonclick()
