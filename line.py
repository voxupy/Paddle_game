from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(0, -290)
        self.pendown()
        self.setheading(90)
        for i in range(17):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()