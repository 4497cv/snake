%
import turtle
import time
import random

delay = 1/60

class Snake:
    obj = turtle.Turtle()
    move_right = 0
    move_left = 0
    move_up = 0
    move_down = 0
    snake_size = 0
    segments = []
    
    def __init__(self):
        self.obj.speed(0)
        self.obj.shape("square")
        self.obj.color("green")
        self.obj.shapesize(stretch_wid=1, stretch_len=1)
        self.obj.penup()
        self.obj.goto(-350,0)
        self.obj.dx = 20
        self.obj.dy = 20
        self.new_segment()
        self.snake_up()
        
    def snake_up(self):    
        if(self.move_up == 0):
            self.move_right = 0
            self.move_left = 0
            self.move_up = 1
            self.move_down = 0

            if(self.obj.dy < 0):
                self.obj.dy*=-1
                
    def snake_down(self):
        if(self.move_down == 0):
            self.move_right = 0
            self.move_left = 0
            self.move_up = 0
            self.move_down = 1
            
            if(self.obj.dy > 0):
                self.obj.dy*=-1
            
    def snake_right(self):
        if(self.move_right == 0):
            self.move_right = 1
            self.move_left = 0
            self.move_up = 0
            self.move_down = 0
            if(self.obj.dx < 0):
                self.obj.dx*=-1
                
    def snake_left(self):
        if(self.move_left == 0):
            self.move_right = 0
            self.move_left = 1
            self.move_up = 0
            self.move_down = 0
            if(self.obj.dx > 0):
                self.obj.dx*=-1

    def move_snake(self):
        last_x = self.obj.xcor()
        last_y = self.obj.ycor()
        if(len(self.segments) > 0):
            self.segments[0].goto(last_x, last_y)
            
        if(self.move_up == 1 or self.move_down == 1):
            self.obj.sety(self.obj.ycor() + self.obj.dy)
            if(self.move_up == 1):
                offset = -15
            else:
                offset = 15
            for index in range(len(self.segments)-1, 0, -1):
                x = self.segments[index-1].xcor()
                y = self.segments[index-1].ycor()
                self.segments[index].goto(x, y)
                self.segments[index].st()
        elif(snake.move_right == 1 or self.move_left == 1):
            self.obj.setx(self.obj.xcor() + self.obj.dx)
            if(self.move_right == 1):
                offset = -15
            else:
                offset = 15
            for index in range(len(self.segments)-1, 0, -1):
                x = self.segments[index-1].xcor()
                y = self.segments[index-1].ycor()
                self.segments[index].goto(x, y)
                self.segments[index].st()

    def new_segment(self):
        self.snake_size+=1
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        new_segment.ht()
        self.segments.append(new_segment)

    def hide_snake(self):
        for index in range(len(self.segments)-1, 0, -1):
           self.segments[index-1].st()
        

# create window
window = turtle.Screen()
window.title("snake game")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

#define snake object
snake = Snake()

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.penup()
ball.goto(random.randrange(-300,300,15),random.randrange(-300,300,15))

window.listen()
window.onkeypress(snake.snake_up,"Up")
window.onkeypress(snake.snake_down,"Down")
window.onkeypress(snake.snake_left,"Left")
window.onkeypress(snake.snake_right,"Right")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {}".format(snake.snake_size), align="center", font=("Courier", 24, "normal"))
while True:
    #move ball
    #snake.setx(snake.xcor() + snake.dx)
    #snake.sety(snake.ycor() + snake.dy)

    for segment in snake.segments:
        if segment.distance(snake.obj) < 20:
            time.sleep(1)
            snake.move_right = 0
            snake.move_left = 0
            snake.move_up = 0
            snake.move_down = 0
            snake.segments.clear()
            snake.obj.clear()
            window.bye()

    window.update()
    pen.clear()
    pen.write("Score: {}".format(snake.snake_size-1), align="center", font=("Courier", 10, "normal"))
    
    snake.move_snake()

    if snake.obj.ycor() > 290:
        snake.obj.sety(-290)

    if snake.obj.ycor() < -290:
        snake.obj.sety(290)

    if snake.obj.xcor() > 390:
        snake.obj.setx(-390)

    if snake.obj.xcor() < -390:
        snake.obj.setx(390)

    if((ball.xcor()+15 > snake.obj.xcor()) and (ball.xcor()-15  < snake.obj.xcor())):
        if((ball.ycor()+15  > snake.obj.ycor()) and (ball.ycor()-15  < snake.obj.ycor())):
            ball.goto(random.randint(-250,250),random.randint(-250,250))
            snake.new_segment()

    #print(snake.xcor(),snake.ycor())
    time.sleep(delay)

