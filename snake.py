from turtle import Turtle
start_position = [(0, 0), (-20, 0), (-40, 0)]
travel = 20

class Snake:
    def __int__(self):
        self.start = []
        self. create_snake()

    def create_snake(self):
        for place in start_position:
            square = Turtle("square")
            square.penup()
            square.goto(place)
            self.start.append(square)

    def move(self):
        for place_num in range(len(self.start) -1, 0, -1):
            x_axis = self.start[place_num-1].xcor()
            y_axis = self.start[place_num-1].ycor()
            self.start[place_num].goto(x_axis, y_axis)
        self.start[0].forward(travel)