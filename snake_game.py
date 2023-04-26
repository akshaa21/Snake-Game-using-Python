import turtle
import time
import random

delay=0.1
score=0
highscore=0

# creating screen
s=turtle.Screen()
s.title("SNAKE GAME")
s.bgcolor("#80ff00")
s.setup(width=750 , height=750)
s.tracer(0)

#creating snake head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#001133")
head.fillcolor("#0055ff")
head.penup()
head.goto(0,0)
head.direction="stop"

#creating food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#660033")
food.fillcolor("#ff0000")
food.penup()
food.goto(0,100)

#Creating Score board
sb=turtle.Turtle()
sb.speed(0)
sb.shape("square")
sb.color("black")
sb.penup()
sb.hideturtle()
sb.goto(0,300)
sb.write("Score : 0  Highscore : 0", align="center",font=("candara", 24, "bold"))

#assign direction
def goup():
    if head.direction!="down":
        head.direction="up"
def godown():
    if head.direction!="up":
        head.direction="down"
def goright():
    if head.direction!="left":
        head.direction="right"
def goleft():
    if head.direction!="right":
        head.direction="left"

def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20) 
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
    
s.listen()
s.onkeypress(goup,"w")
s.onkeypress(godown,"s")
s.onkeypress(goright,"d")
s.onkeypress(goleft,"a")

bodies = []

#main loop
while True:
    s.update()
    if head.xcor() > 374 or head.xcor() < -374 or head.ycor() > 374 or head.ycor() < -374:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        print("GAME OVER")
        for body in bodies:
            body.goto(500, 500)
        bodies.clear()
        score = 0
        delay = 0.1
        sb.clear()
        sb.write("Score : {}  Highscore : {} ".format( score, highscore), align="center", font=("candara", 24, "bold"))
      
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

 
        # Adding segment
        body = turtle.Turtle()
        body.speed(0)
        body.shape("circle")
        body.color("#0000FF")  # tail colour
        body.fillcolor("#7FFFD4")
        body.penup()
        bodies.append(body)
        score += 10
        delay -= 0.001
        if score > highscore:
            highscore = score
        sb.clear()
        sb.write("Score : {}   Highscore : {} ".format(score, highscore), align="center", font=("candara", 24, "bold"))
        
    
    # Checking for head collisions with body segments
    for index in range(len(bodies)-1, 0, -1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x, y)
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    move()
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            print("GAME OVER")
            for body in bodies:
                body.goto(1000, 1000)
            bodies.clear()
            score = 0
            delay = 0.1
            sb.clear()
            sb.write("Score : {}  Highscore : {} ".format(score, highscore), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
s.mainloop()



                
    
