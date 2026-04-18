from turtle import *


shape('circle')
#we want to paint a house

#step 1:draw a square
speed(30)
width(5)
color('gray')



forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end og square

#drawing a door

forward(80)
color('green')
begin_fill()

left(90)
forward(75)  #height of the door
right(90)
forward(35)
right(90)
forward(75)
end_fill()
penup()
goto(200,200)
pendown()

color('brown')

begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(165,160)
left(30)
pendown()

begin_fill()

color('blue')
forward(43)
right(90)
forward(43)
right(90)
forward(43)
right(90)
forward(43)
end_fill()

penup()
goto(32,160)
pendown()

begin_fill()
forward(43)
right(90)
forward(43)
right(90)
forward(43)
right(90)
forward(43)
end_fill()

#buxari

width(3)
penup()
goto(165,265)
pendown()
color('black')
begin_fill()

forward(42)
right(90)
forward(22)
right(90)
forward(78)
right(150)
forward(42.50)
end_fill()






exitonclick()
