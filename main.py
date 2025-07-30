import time
from turtle import  Screen
from snake import Snake

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game.")

snake = Snake()


game_is_on = True
screen.listen()
screen.onkey(snake.up, "Up" )
screen.onkey(snake.down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")



while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()