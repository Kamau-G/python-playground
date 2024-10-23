"""
Algorithm:

draw triangle
    Repeat 4 times:
        forward 100
        right 120
draw hexagon
    Repeat 6 times:
        draw triangle
        left 60
"""

import turtle

#set up basic turtle
t = turtle.Turtle()
wn = turtle.Screen()
#
def drawTriangle(distance):
    for count in range(3):
        t.fd(distance)
        t.rt(120)
#
def drawHexagon():
    for count in range(6):
        drawTriangle(100)
        t.lt(60)
#
drawHexagon()

wn.exitonclick()

"""
Algorithm:
Draw square
    repeat 4 times
        Forward 100
        Left 90
draw row
    reapeat x 3
        draw square
        forward 100
draw shape
    draw row
    Pen up
    reset position
    move turtle up 100
    Pen Down
    draw row
    Pen up
    reset position
    move turtle up 200
    Pen down
    draw row
"""

import turtle
wn = turtle.Screen()
t = turtle.Turtle()


def drawSquare():
    for count in range(4):
        t.fd(100)
        t.lt(90)
#
def drawRow():
    for count in range(3):
        drawSquare()
        t.fd(100)
#
def drawShape():
    drawRow()
    t.pu()
    t.goto(0,100)
    t.pd()
    drawRow()
    t.pu()
    t.goto(0,200)
    t.pd()
    drawRow()
#
drawShape()
t.pu()
t.goto(0,0)
wn.exitonclick()

"""
Algorithm:

draw Cross
    forward 100
    back 25
    left 90
    forward 50
    back 100
    reset position
draw shape
    repeat draw cross x 4
"""

import turtle

wn = turtle.Screen()
t = turtle.Turtle()

def drawCross():
    t.fd(100)
    t.bk(25)
    t.lt(90)
    t.fd(25)
    t.bk(50)
    t.pu()
    t.goto(0,0)
    t.pd()

for count in range(4):
    drawCross()


wn.exitonclick()

"""
Algorithm:
Repeat 4 times:
    Forward 100
        Repeat 3 times:
            Left turn 90
            Forward 100
            Right turn 90
            Forward 100
    Left turn 90

"""

import turtle
#
#set up basic turtle
t = turtle.Turtle()
wn = turtle.Screen()
#
def step():
    t.fd(100)
    for count in range(3):
        t.lt(90)
        t.fd(100)
        t.rt(90)
        t.fd(100)
    t.lt(90)
for count in range(4):
    step()

wn.exitonclick()

