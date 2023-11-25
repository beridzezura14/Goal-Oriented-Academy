print("Zura Beridze")

from turtle import *

# speed(20)
width(4)

# It is a building

color("gray")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()

# It is a door

left(90)
forward(70)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

# It is a roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# It is a left window
penup()
goto(20, 60)
pendown()

color("yellow")
begin_fill()
right(150)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)

# It is a right window

penup()
goto(150, 60)
pendown()

right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
end_fill()

# land
penup()
goto(-100, 0)
pendown()

color("green")
begin_fill()
left(90)
forward(10)
left(90)
forward(400)
left(90)
forward(10)
left(90)
forward(400)
end_fill()












exitonclick()