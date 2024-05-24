from turtle import Turtle
FONT=("Courier", 15, "bold")
ALIGN="center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.up()
        self.goto(0,270)
        self.hideturtle()
        self.display()
        
    ######################(Displaying Score)######################
    def display(self):
        self.write(f"Score: {self.score} ", align=ALIGN, font=FONT)
        
    #####################(Incrementing Score)#####################
    def increment(self):
        self.score += 1
        self.clear()
        self.display()

    #######################(Game End)###########################
    def end(self):
        self.color("yellow")
        self.up()
        self.goto(0,0)
        self.hideturtle()
        self.write(f"GAME OVER!\nYour Final Score: {self.score} ", align=ALIGN, font=FONT)
    

