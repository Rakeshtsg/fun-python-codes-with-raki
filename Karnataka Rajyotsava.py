from turtle import *

bgcolor('black')
pensize(6)
color('white')

rt(90)
fd(200)
lt(180)
fd(350)
rt(90)

pensize(2)
begin_fill()

fd(200)
rt(90)
fd(50)
rt(90)
fd(200)
color('yellow')
end_fill()

color('white')
begin_fill()
rt(90)
fd(50)
rt(180)
fd(100)
lt(90)
fd(200)
lt(90)
fd(50)

color('red')
end_fill()

hideturtle()
penup()
lt(180)
fd(150)
rt(90)
fd(150)
pendown()
color('white')
write('ಕರ್ನಾಟಕ ರಾಜ್ಯೋತ್ಸವ',font=('arial',22,'normal'))    #font size for pc 12 
done()