from turtle import Turtle

initial_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

up = 90
down = 270
right = 0
left = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snack()
        self.head = self.segments[0]
    def create_snack(self):

        for position in initial_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0 , -1):

            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def turn_right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def turn_left(self):
        if self.head.heading() != right:
            self.head.setheading(left)









