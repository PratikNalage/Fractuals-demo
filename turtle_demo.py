import turtle
'''
def draw_square():
    window = turtle.Screen()
    window.bgcolor('red')
    a = turtle.Turtle()
    a.shape('turtle')
    a.forward(100)

draw_square()
'''

def draw_art():
    window = turtle.Screen()
    window.bgcolor('cyan')
    o = turtle.Turtle()
    o.shape('turtle')
    o.speed(100)
    for i in range(72):
        for j in range(4):
            o.forward(150)
            o.right(90)
        o.right(5)

#draw_art()

def draw_art1():
    window = turtle.Screen()
    window.bgcolor('cyan')
    o = turtle.Turtle()
    o.shape('turtle')
    o.speed(100)
    l=150
    for i in range(1,72):
        for j in range(3):
            o.forward(l/i)
            o.left(120)
        o.forward(l/(4*i))

draw_art1()
