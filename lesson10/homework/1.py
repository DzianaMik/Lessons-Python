'''
Добавить несколько черепах 
    - или сразу 
    * или в течении игры по одной через определенное количество кликов
    - на каждой забиндить клик через одну и туже функцию cath

'''

import turtle
import random
def catch(x,y):
    print("Поймали черепаху!")
turtles = []
for _ in range(5):
    t = turtle.Turtle(shape="turtle")
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.onclick(catch)  
    turtles.append(t)
turtle.done()


