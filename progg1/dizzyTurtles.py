import turtle
import random


def rectangle(x, y, width, height, color):
    '''
    Gör rektangel
    '''
    t = make_turtle(x, y)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    for dist in [width, height, width, height]:
        t.forward(dist)
        t.left(90)
    t.end_fill()
    
def make_turtle(x, y):
    '''
    Creates the object
    '''
    t = turtle.Turtle()
    jump(t, x, y)
    #visible /= t.hideturtle()
    t.speed(0)
    return t

def jump(t, x, y):
    '''
    Move without leaving behind a line
    '''
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def random_turtle(low=-250, high=250):
    """Creates and returns a random turtle.

       Random position,
       random heading and
       random color.
       
    """
    t = turtle.Turtle()
    moveto(t, randint(low, high), randint(low, high))
    t.setheading(randint(0, 359))
    t.speed(0)                              #
    t.color(random(), random(), random())   
    return t

    
def move_random(t):
    t.left(random.randint(-45,45))
    t.forward(random.randint(0,25))
    x, y = t.pos()
    if abs(x) > 230 or abs(y) > 230:
        t.setheading(t.towards(0, 0))
        
side = 500
rectangle(-side/2,-side/2,side,side,color='teal')
close = 0
p = []
for i in range(4):
    p.append(random.randint(-side/2,side/2))
t = [t1,t2] = [make_turtle(p[0],p[1]), make_turtle(p[2],p[3])]


for i in range(500):
    move_random(t[0])
    move_random(t[1])
    if (t[0].distance(t[1])) < 50:
            t[0].write("Close")
            t[1].write("Close")
            close = close + 1
print(f'Close = {close}')

    
