# import turtle module <======
import turtle

# make game win
win = turtle.Screen()
# make title win
win.title('ping pong gmae')
# make backGround win
win.bgcolor('#222')
# make width And height win
win.setup(width=800, height=600)
# dont update win
win.tracer(0)


# racket One
racketOne = turtle.Turtle()
racketOne.speed(0)
racketOne.shapesize(stretch_wid=7, stretch_len=1)
racketOne.shape('square')
racketOne.color('red')
racketOne.penup()
racketOne.goto(-350, 0)

# racket two
racketTwo = turtle.Turtle()
racketTwo.speed(0)
racketTwo.shapesize(stretch_wid=7, stretch_len=1) # set the stretch to get your size
racketTwo.shape('square')
racketTwo.color('green')
racketTwo.penup()
racketTwo.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0) # set speed on animation
ball.shape('square') # set shape
ball.color('#eee') # set color
ball.penup() 
ball.goto(0, 0)

# racketOne function <=====

# racketOne to up
def racketOne_up():
    y = racketOne.ycor()
    y += 20
    racketOne.sety(y)
# racketOne to down
def racketOne_down():
    y = racketOne.ycor()
    y -= 20
    racketOne.sety(y)

# racketTwo to up
def racketTwo_up():
    y = racketTwo.ycor()
    y += 20
    racketTwo.sety(y)
# racketTwo to down
def racketTwo_down():
    y = racketTwo.ycor()
    y -= 20
    racketTwo.sety(y)

# keyboard bindings function
win.listen()
win.onkeypress(racketOne_up, 'w') # racketOne to up
win.onkeypress(racketOne_down, 's') # racketOne to down
win.onkeypress(racketTwo_up, 'Up') # racketOne to up
win.onkeypress(racketTwo_down, 'Down') # racketOne to down

# game loop
while True:
    win.update()