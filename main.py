from turtle import Turtle,Screen

def moveahead():
    t.forward(20)

def movebehind():
    t.backward(20)
    

def moveanti():
    t.left(20)
    t.forward(20)
    
def moveclock():
    t.right(20)
    t.forward(20)

def rest():
    t.reset()


t=Turtle()
s=Screen()
s.listen()
s.onkey(key="W",fun=moveahead)
s.onkey(key="S",fun=movebehind)
s.onkey(key="A",fun=moveanti)
s.onkey(key="D",fun=moveclock)
s.onkey(key="C",fun=rest)




s.exitonclick()