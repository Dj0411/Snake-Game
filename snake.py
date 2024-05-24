from turtle import Turtle
move_dist=20
snake_gap=-20
class Snake:
    def __init__(self):
        self.snakes=[]
        self.create_snake()
        self.head=self.snakes[0]

    #####################(Creating Snake)#######################
    def create_snake(self):
        for i in range(3):
            if(i==0):
                t1=Turtle(shape="triangle")
            else:
                t1=Turtle(shape="square")
            t1.up()
            t1.color("white")
            t1.setpos(snake_gap*i,0)
            self.snakes.append(t1)
            
    ####################(increasng length)#######################
    def len_increment(self):
            t1=Turtle(shape="square")
            t1.up()
            t1.color("white")
            x_pos=self.snakes[len(self.snakes)-1].xcor()
            y_pos=self.snakes[len(self.snakes)-1].ycor()
            t1.setpos(x_pos,y_pos)
            self.snakes.append(t1)
            
    #####################(Snake Move continuously)##############
    def move(self):
        for seg in range(len(self.snakes)-1, 0, -1):
            new_x=self.snakes[seg-1].xcor()
            new_y=self.snakes[seg-1].ycor()
            self.snakes[seg].goto(new_x,new_y)
        self.head.fd(move_dist)

    #####################(Changing Snake Direction)###############
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
