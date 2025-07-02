"""import turtle
import colorgram

colors = colorgram.extract("image.jpg",15)
vals=[]
for x in colors:
    r= x.rgb.r
    g= x.rgb.g
    b= x.rgb.b
    clr = (r,g,b)
    vals.append(clr)
print(vals)
for y in vals:
    if y[0]>237 and y[1]>237 and y[2]>237 :
        vals.pop(vals.index(y))
print(vals)"""

color_list=[(238, 254, 249), (23, 16, 94), (232, 43, 6), (153, 14, 30), (41, 181, 158), (127, 253, 206), (237, 71, 166), (209, 179, 208), (246, 218, 21), (40, 133, 242), (246, 218, 5), (207, 148, 178)]
import turtle
import random
tutu = turtle.Turtle()
turtle.colormode(255)
turtle.speed(50)

def draw_spots():
    for x in range(8):
        for y in range(len(color_list)+1):
            tutu.dot(20,random.choice(color_list))
            tutu.up()
            tutu.forward(50)
            tutu.down()
            if x%2==0 and y==len(color_list):
                tutu.dot(20, random.choice(color_list))
                tutu.left(90)
                tutu.up()
                tutu.fd(50)
                tutu.down()
                tutu.left(90)
            elif x%2==1 and y==len(color_list):
                tutu.dot(20, random.choice(color_list))
                tutu.right(90)
                tutu.up()
                tutu.fd(50)
                tutu.down()
                tutu.right(90)
    screen = turtle.Screen()
    screen.exitonclick()

draw_spots()

