######## Mandala Art (Python) ########
import turtle
t=turtle.Turtle()
t.speed(300)
turtle.bgcolor('black')
col = ['green','red','blue','lime']
for c in range(100):
    for x in range(10):
        t.width(3)
        t.color(col[c%3])
        t.circle(100)
        t.left(5)
turtle.done()
