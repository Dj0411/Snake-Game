from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

#######################################################
s=Screen()
s.setup(width=600,height=600)
s.title("<--<--My Snake Game-->-->")
s.bgcolor("black")
s.tracer(0)

#####################(Class Objects)###################
snake=Snake()
food=Food()
scoreboard= Score()

#####################(Listen to keypress)####################
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

#######################(Moving the snake)##################
game_on=True
while game_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    if(snake.head.distance(food) < 17):
        food.food_location()
        scoreboard.increment()
        snake.len_increment()
        print("Khaa GYa mota")

    if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.end()
        game_on=False

    for part in snake.snakes[1:]:
        if(snake.head.distance(part) < 10):
            game_on=False
            scoreboard.end()        
        
s.exitonclick()
#######################################################

