import turtle

side_length=246.7534
size=3
def drawtriangle(side_length):
    for x in range(0,size):
        turtle.forward(side_length)
        turtle.left(120)

drawtriangle(side_length)
