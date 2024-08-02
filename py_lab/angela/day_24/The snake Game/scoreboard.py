from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("High Score.txt","r") as file:
            self.high_score=int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   |   High Score: {self.high_score}", align=ALIGNMENT, font=("arial",20))


    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            self.score=0
            self.update_scoreboard()
            with open("High Score.txt","w") as file:
                file.write(f"{self.high_score}")
        else:
            self.score=0
            self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
