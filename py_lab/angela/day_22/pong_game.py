from turtle import Screen,Turtle
from pong import Pong
from player import Player
from time import sleep
from score import Score,Splitter

screen=Screen()
screen.setup(width=1035,height=535)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

splitter=Splitter()
score=Score()

pong=Pong()

player_r=Player("left")
player_l=Player("right")

screen.onkeypress(lambda :player_r.to_up(),"Up")
screen.onkeypress(lambda :player_r.to_down(),"Down")
screen.onkeypress(lambda :player_l.to_up(), "r")
screen.onkeypress(lambda :player_l.to_down(),"f")

def playing():
    pong.goto(0,0)
    while True:
        pong.move()
        if pong.distance(player_r)<40 and pong.xcor()>480:
            pong.to_left()
        elif pong.distance(player_l)<40 and pong.xcor()<-490:
            pong.to_right()
        elif pong.xcor()>520:
            score.player1_scored()
            playing()
        elif pong.xcor()<-530:
            score.player2_scored()
            playing()
        sleep(0.03)
        screen.update()
playing()


screen.mainloop()
