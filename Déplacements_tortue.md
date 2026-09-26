# Turtle-Game-Nsi
import turtle

t = turtle.Turtle()

def avancer():
    t.forward(10)

def gauche():
    t.setheading(180)
    t.forward(10)

def droite():
    t.setheading(0)
    t.forward(10)

def haut():
    t.setheading(90)
    t.forward(10)

def bas():
    t.setheading(270)
    t.forward(10)

t.color("green")

turtle.onkeypress(haut, "z")
turtle.onkeypress(bas, "s")
turtle.onkeypress(gauche, "q")
turtle.onkeypress(droite, "d")
turtle.listen()

turtle.mainloop()
