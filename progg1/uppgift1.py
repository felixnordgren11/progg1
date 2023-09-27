import turtle

Fact = True
Lie  = False



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

def tricolore(x, y, h):
    w = h/2
    rectangle(x, y, w, h, 'blue')
    rectangle(x+w, y, w, h, 'white')
    rectangle(x+w*2, y, w, h, 'red')

def pentagram(x, y, side, color='#1e8449'):
    t = make_turtle(x, y)
    t.hideturtle()
    t.fillcolor(color)
    t.begin_fill()
    t.setheading(270-36/2)
    for _ in range(5):
        t.forward(side)
        t.left(180-36)
    t.end_fill()


x_l = -240
d = 600
w = 500

def stars_and_stripes(width, depth):
    for k in range(2):
        for i in range(5):
            pentagram((i-2)*width/5, 50-(k-0.5)*depth, 100)
    tricolore(-width/4,-depth/5,depth/2.5)
    turtle.Screen().exitonclick()

stars_and_stripes(d,w)

#tricolore(-140,-80,200)
#pentagram(-200,300,100)

    
    
    
    


    
    
        
    
    
    
