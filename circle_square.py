import turtle

sq = turtle.Turtle()
sq.speed(1)

def cre():
    for i in range(4):
        sq.forward(100)
        sq.right(5)
def lop():
    for i in range(30):
        cre()
lop()