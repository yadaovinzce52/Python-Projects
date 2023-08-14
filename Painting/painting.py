# import colorgram as cg
#
# colors = cg.extract('image.jpg', 2**32)
#
# color_palette = []
#
# for i in range(len(colors)):
#     rgb = colors[i].rgb
#     if rgb.r > 240 and rgb.g > 240 and rgb.b > 240:
#         continue
#     else:
#         color_palette.append((rgb.r, rgb.g, rgb.b))
#
# print(color_palette)
from turtle import Turtle, Screen
from random import choice

color_palette = [(61, 103, 137), (105, 166, 204), (17, 29, 53), (107, 96, 82), (33, 28, 17), (3, 164, 245),
                 (186, 226, 248), (50, 60, 83), (157, 145, 130), (92, 85, 90), (42, 34, 39), (98, 104, 101),
                 (14, 22, 15), (79, 74, 28), (103, 129, 156), (154, 136, 77), (138, 143, 141), (146, 140, 144),
                 (151, 197, 234), (69, 59, 67), (136, 205, 244), (73, 60, 56), (221, 199, 128), (11, 78, 111),
                 (121, 131, 127), (136, 124, 120), (55, 71, 53), (132, 124, 129), (197, 189, 187), (186, 194, 192),
                 (195, 189, 193), (239, 199, 13)]


def random_color():
    color = choice(color_palette)
    return color


t1 = Turtle()
screen = Screen()
screen.colormode(255)
t1.hideturtle()
t1.penup()
t1.goto(-100, -100)
t1.speed('fastest')

for _ in range(10):
    for _ in range(10):
        color = random_color()
        t1.dot(20, color)
        t1.forward(50)
    t1.left(90)
    t1.forward(50)
    t1.left(90)
    t1.forward(500)
    t1.left(180)

screen.exitonclick()
