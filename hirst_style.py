import turtle as turtle_module
import random
from PIL.ImageChops import screen

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed(100)
tim.penup()
tim.hideturtle()
color_list = [(251, 249, 241), (253, 244, 250), (238, 252, 244), (237, 243, 250), (241, 231, 59), (218, 156, 92), (201, 7, 31), (184, 68, 29), (40, 93, 171), (233, 50, 127), (236, 230, 2), (40, 213, 82), (96, 180, 215), (17, 22, 56), (33, 34, 160), (198, 13, 7), (226, 154, 10), (51, 25, 11), (216, 135, 173), (104, 235, 170), (88, 210, 136), (190, 37, 95), (24, 144, 28), (230, 64, 44), (73, 8, 52), (12, 198, 219), (238, 159, 196), (92, 73, 9), (241, 168, 159), (87, 87, 210)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1,num_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

for i in range(10+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

screen=turtle_module.Screen()
screen.exitonclick()
