""" 
Author Name: James Teerlink 
Course: CS 1400 Fundamentals of Programming
Project 2: Geometric Shapes - Dungeon's and Dragons Dice
Due Date: 9/22/2018
No help was used while writing this code

Use the turtle module to draw five different geometric shapes that you choose:
Major steps:
0. import turtle module
1. Intantiate the window object with the turtle.Screen() function.
2. Create 5 different turtles to draw five different geometric shapes.
3. Move each turtle to different areas of the screen before starting.
4. Go through individually to have each turtle draw their shape one at a time. 
5. Create a multidimensional Array for each turtle for the for loop to loop through to get different coordinates and colors to fill 
    the surface of each facet on the dice. 
6. Close the window object when user clicks on the screen.

Bullet Points and Lessons Learned:
0. I have some Dungeon and Dragon dice that I looked at while writing this code to see their shapes. 
1. I used the formula ((n-2)*180°)/n = interior angle in degrees to know how much to turn the turtles in the for loops
2. I needed to draw the outer geometric shape first and use .write() function to get all the coordinates for the boundary to draw with.
3. Next I drew the inner geometric shape to get the coordinates of each corner 
4. Sometimes I needed to use a little geometry to make the process go a little faster but mostly I was able to just use goto() function
    to move the turtles and draw a line between the corners of the inner and outer geometric shapes. 
5. I found that it was clearer in my head to keep all the coordinates in one place for the multidimensional arrays and loop through them
    for each surface so that I could keep it organized while I wrote the code. It seemed to make for less code to me. 
"""

#import turtle
import turtle

#instantiate the window object
wn = turtle.Screen()

#create turtle number 1
one = turtle.Turtle()
one.color("green")
one.hideturtle()

#create turtle number 2
two = turtle.Turtle()
two.color("red")
two.hideturtle()

#create turtle number 3
three = turtle.Turtle()
three.color("blue")
three.hideturtle()

#create turtle number 4
four = turtle.Turtle()
four.color("purple")
four.hideturtle()

#create turtle number 5
five = turtle.Turtle()
five.color("orange")
five.hideturtle()

#draw first shape with first turtle
#move turtle into position
one.penup()
one.left(90)
one.fd(275)
one.left(45)
one.pendown()

#Draw outer geometric shape
for i in range(4):
    one.left(90)
    one.fd(100)

#Draw inner geometric shape and loop through array to make different surfaces different colors
one.left(135)
one.begin_fill()
one.forward(70.71)
one.left(90)
one.fd(70.71)
one.end_fill()
d8 = ["#6B8E23", "#90EE90", "#9ACD32"]
for i in d8:
    one.color(i)
    one.begin_fill()
    one.back(70.71)
    one.right(90)
    one.fd(70.71)
    one.end_fill()

#Draw second geometric shape with second turtle
#Get turtle into position
two.penup()
two.left(90)
two.fd(50)

#Draw inner geometric shape and loop through array to make different surfaces different colors
d4 = [[0.0, 103.92, -60.0, 0.0, 0.0, 50.0, "#FA8072"], \
        [-60.0, 0.0, 60.0, 0.0, 0.0, 50.0, "#FF4500"], \
        [60.0, 0.0, 0.0, 103.92, 0.0, 50.0, "red"]]

for i in d4:
    two.pendown()
    two.color(i[6])
    two.begin_fill()
    two.goto(i[0], i[1])
    two.goto(i[2], i[3])
    two.goto(i[4], i[5])
    two.end_fill()

#Draw third shape with third turtle
#Move turtle into position
three.penup()
three.fd(150)
three.pendown()
three.left(18)

#Draw outer geometric shape
for i in range(10):
    three.fd(50)
    three.left(36)
   
three.penup()
three.goto(150.00, 47.0)    
three.right(18)
three.pendown()
three.fd(25)
three.color("blue")
three.begin_fill()
for i in range(5):
    three.left(72)
    three.fd(50)
three.end_fill()
    
#Draw inner geometric shape and loop through array to make different surfaces different colors

d12 = [[150, 123.94, 150, 161.80, 197.55, 146.35, 226.94, 106.90, 190.45, 94.55, "#ADD8E6"], \
        [190.45,94.55,226.94,105.90,226.94,55.90,197.55,15.45,175,47, "#1E90FF"], \
        [175.00, 47.00, 197.55, 15.45,150,0,102.45,15.45,125,47, "#4682B4"], \
        [125.00, 47, 102.45, 15.45,73.06,55.90,73.06,105.90,109.55,94.55, "#4169E1"], \
        [109.55, 94.55, 73.06, 105.90,102.45,146.35,150,161.80,150,123.94, "#191970"]]

for i in d12:
    three.penup()
    three.goto(i[0], i[1])
    three.pendown()
    three.color(i[10])
    three.begin_fill()
    three.goto(i[2], i[3])
    three.goto(i[4], i[5])
    three.goto(i[6], i[7])
    three.goto(i[8], i[9])
    three.end_fill()

#Draw fourth shape with fourth turtle
#Get turtle into position
four.penup()
four.back(150)
four.pendown()
four.left(18)

#Draw outer geometric shape
for i in range(10):
    four.fd(50)
    four.left(36)

four.penup()
four.goto(-150.0, 80.905)
#Draw inner geometric shape and loop through array to make different surfaces different colors

d10 = [[-197.55, 146.35, -150.0, 161.80, -102.45, 146.35, -150.0, 80.905, "#9370DB"], \
        [-102.45, 146.35, -73.06, 105.90, -73.06, 55.90, -150.0, 80.905, "#D8BFD8"], \
        [-73.06, 55.90, -102.45, 15.45, -150.0, 0.0, -150.0, 80.905, "#DA70D6"], \
        [-150.0, 0, -197.55, 15.45, -226.94, 55.90, -150.0, 80.905, "#9932CC"], \
        [-226.94, 55.90, -226.94, 105.90, -197.55, 146.35, -150.0, 80.905, "#4B0082"]]


four.pendown()
for i in d10:
    four.color(i[8])
    four.begin_fill()
    four.goto(i[0], i[1])
    four.goto(i[2], i[3])
    four.goto(i[4], i[5])
    four.goto(i[6], i[7])
    four.end_fill()


#Draw fifth and final shape with fifth turtle
#Get turtle into position
five.right(90)
five.penup()
five.fd(25)
five.right(60)
five.pendown()

#Draw outer geometric shape
for i in range(6):
    five.fd(100)
    five.left(60)
five.penup()
five.goto(0, -185)
five.seth(90)
five.right(30)
five.pendown()

#Draw inner geometric shape and loop through array to make different surfaces different colors
five.begin_fill()
for i in range(3):
    five.fd(110)
    five.left(120)
five.end_fill()

d20 = [ [0.0, -225.00, 86.6, -175.0, 0.0, -185.0, "orange"],\
        [55.00, -89.74, 86.60, -175.00, 0.0, -185.00, "gold"], \
        [0.0, -225.00, -86.6, -175.00, 0.0, -185.0, "red"], \
        [-55.00, -89.74, -86.60, -175, 0.0, -185.0, "orangered"], \
        [-55.0, -89.74, -86.6, -75.0, -86.6, -175.0, "maroon"], \
        [-55.0, -89.74, -86.6, -75.0, 0.0, -25.0, "indianred"], \
        [-55.0, -89.74, 55.0, -89.74, 0.0, -25.0, "gold"], \
        [55.0, -89.74, 86.6, -75.0, 0.0, -25.0, "darkorange"], \
        [55.0, -89.74, 86.6, -175.0, 86.6, -75.0, "yellow"]
        ]

for i in d20:
    five.pendown()
    five.color(i[6])
    
    five.goto(i[0], i[1])
    five.begin_fill()
    five.goto(i[2], i[3])
    five.goto(i[4], i[5])
    five.end_fill()

#Enable user to close the window object when they click on the screen after all turtles are finished drawing
wn.exitonclick()