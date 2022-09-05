from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score(self.score)
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)

    def increase_score(self, score=1):
        self.score += score
        self.clear()
        self.update_scoreboard()

    def read_high_score(self):
        with open("data.txt", "r") as file:
            data = file.read()
            if not data.isnumeric():
                self.high_score = 0
            else:
                self.high_score = int(data)

    def write_high_score(self, high_score):
        with open("data.txt", "w") as file:
            file.write(str(high_score))
