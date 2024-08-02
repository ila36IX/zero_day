from turtle import Turtle,Screen
from random import randint,choice

class Pong(Turtle):
    def __init__(self,speed=0,w=1000,h=500):
        super().__init__()
        self.up()
        self.speed(speed)
        self.shape("circle")
        self.shapesize(0.6,0.6)
        self.color("white")
        self.w=w
        self.h=h

    def to_right(self):
        self.seth(choice([randint(0,45),randint(315,370)]))

    def to_left(self):
        self.seth(randint(135,225))

    def to_bottom(self):
        hd= self.heading()
        self.seth(360-hd)

    def to_above(self):
        hd=self.heading()
        self.seth(360-hd)

    def move(self): 
        self.fd(10)
        if self.ycor()>200:
            self.to_bottom()
        elif self.ycor() < -250 :
            self.to_above()



