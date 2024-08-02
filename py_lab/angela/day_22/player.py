from turtle import Turtle,Screen





class Player(Turtle):
    def __init__(self,side):
        super().__init__()
        if side == "left":
            self.goto(500,0)
        elif side=="right":
            self.goto(-510,0)
        self.color("white")
        self.up()
        self.shapesize(4,0.3)
        self.shape("square")

    def to_up(self):
        if self.ycor() <220:
            self.goto(self.xcor(),self.ycor()+15)

    def to_down(self):
        if self.ycor()>-220:
            self.goto(self.xcor(),self.ycor()-15)



