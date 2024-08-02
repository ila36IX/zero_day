from turtle import Turtle,Screen
import time

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.ht()
        self.up()
        self.player1=0
        self.player2=0
        self.update_score()
   
    def update_score(self):
        self.clear()
        self.goto(0,210)
        self.write(f"Player 1 : {self.player1}             Player 2 : {self.player2}",align="center",font=("Arial",17))
    
    def player1_scored(self) :
        self.player1+=1
        self.update_score()

    def player2_scored(self) :
        self.player2+=1
        self.update_score()

class Splitter(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.up()
        self.goto(-2,-250)
        self.seth(90)
        for _ in range(40):
            if self.ycor()>220:break
            self.down()
            self.fd(10)
            self.up()
            self.fd(10)

   
