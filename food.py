from turtle import Turtle
import random

def get_random_coords():
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    return (random_x, random_y)
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=.5)
        self.color("yellow")
        self.speed("fastest")
        self.goto(get_random_coords())

    def move(self):
        self.goto(get_random_coords())