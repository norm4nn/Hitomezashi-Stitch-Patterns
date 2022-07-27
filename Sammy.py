import turtle
from turtle import Turtle
from enum import Enum

WIDTH = turtle.window_width()
HEIGHT = turtle.window_height()
TURTLE_SIZE = 20
PADDING = 10
BASIC_DISTANCE = 50

#Directions
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Sammy(Turtle):
    def __init__(self):
        super(Sammy, self).__init__()
        self.speed(2000)
        self.distance = BASIC_DISTANCE
    
    def go_to_upper_left(self):
        self.penup()
        self.setx(-1 * WIDTH // 2 + TURTLE_SIZE)
        self.sety(HEIGHT // 2 - TURTLE_SIZE)
        self.setheading(RIGHT)
        
    
    def draw_grid(self,str1, str2, bin1, bin2):
        self.penup()
        self.go_to_upper_left()
        for i, ch in enumerate(str1):
            self.forward(self.distance)
            self.write(ch, align="left", font=("Arial", 10, "normal"))

        self.go_to_upper_left()
        self.setheading(DOWN)
        for i, ch in enumerate(str2):
            self.forward(self.distance)
            self.write(ch, align="left", font=("Arial", 10, "normal"))
        
        self.go_to_upper_left()
    
        self.forward(PADDING)
        self.setheading(DOWN)
        
        self.pendown()
        for i in range(len(str2) + 1):
            self.forward(self.distance)
        self.setheading(RIGHT)
        for i in range(len(str1) + 1):
            self.forward(self.distance)
        self.penup()

        self.go_to_upper_left()

        self.forward(PADDING)
        self.pendown()
        for i in range(len(str1) + 1):
            self.forward(self.distance)
        self.setheading(DOWN)
        for i in range(len(str2) + 1):
            self.forward(self.distance)

        self.penup()

        # start with drawing lines
        self.go_to_upper_left()
        self.forward(PADDING)

        for i in range(len(bin1)):
            self.setheading(RIGHT)
            self.forward(self.distance)
            self.draw_lines(len(bin2) + 1, bin1[i], DOWN)

        self.penup()

        self.go_to_upper_left()
        self.forward(PADDING)


        for i in range(len(bin2)):
            self.setheading(DOWN)
            self.forward(self.distance)
            self.draw_lines(len(bin1) + 1, bin2[i], RIGHT)

        self.penup()
        self.go_to_upper_left()
        self.forward(PADDING)
        self.hideturtle()


    def draw_lines(self,num_of_steps, start_with_line, direction):
        back_position = self.pos()
        if start_with_line: self.pendown()
        else: self.penup()
        self.setheading(direction)
        for i in range(num_of_steps):
            self.forward(self.distance)

            if self.isdown(): self.penup()
            else: self.pendown()

        self.penup()
        self.setpos(back_position)

    def setting_step(self, str1, str2):

        while self.distance > 0:
            num_steps_horizontal = (WIDTH - 2 * (PADDING + TURTLE_SIZE)) // self.distance - 1
            num_steps_vertical = (HEIGHT - 2 * (PADDING + TURTLE_SIZE)) // self.distance - 1

            if num_steps_horizontal < len(str1) or num_steps_vertical < len(str2):
                self.distance *= .9
                self.distance = int(self.distance)
            else:
                break

        if self.distance == 0:
            self.distance = 1

