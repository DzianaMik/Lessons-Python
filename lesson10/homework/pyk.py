import turtle
import random
def catch(x,y):
    print(f"Ты кликнул по черепахе на позиции {x, y}!")
turtles = []
for _ in range(3):
    t = turtle.Turtle(shape="turtle")
    t.penup()
    t.goto(random.randint(0, 100), random.randint(0, 100))
    t.onclick(catch)  
    turtles.append(t)
turtle.done()
