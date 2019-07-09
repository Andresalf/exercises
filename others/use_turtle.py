import turtle
import random

def tree(branchLen, penSize, t):
    if branchLen > 5:
        t.pensize(penSize)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - random.randrange(1, 16), penSize+1, t)
        t.left(40)
        tree(branchLen - random.randrange(1, 16), penSize+1, t)
        t.right(20)
        t.backward(branchLen)


myWin = turtle.Screen()
t = turtle.Turtle()
t.up()
t.backward(100)
t.down()
t.color("green")
t.left(90)
t.pensize(1)
tree(75, 1, t)
myWin.exitonclick()