from turtle import Turtle

# creating constants to make changes easily
ALIGNMENT = 'center'
FONT = ('Consolas', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup() # to hide the arrow mark while moving up on the next line
        self.goto(0,270) # to print the score on the top.
        self.hideturtle() # to hide the turtle arrow
        self.updating_scoreboard()

    def updating_scoreboard(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT , font=FONT)

    def game_over(self):
        self.goto(0,0) # to show the game over text on the center of the screen
        self.write(" GAME OVER ", align= ALIGNMENT , font=FONT)


    def increasing_score(self):
        self.score += 1
        self.clear()
        self.updating_scoreboard()
