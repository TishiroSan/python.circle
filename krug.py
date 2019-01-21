from graph import *
a=500
b=500
canvasSize(a,b)
r=10 #радиус шарика
c=circle(40,40,r)
mX=1
mY=1
def update():
    global mX
    global mY
    x = xCoord(c)
    y = yCoord(c)
    moveObjectBy(c, mX, mY)
    if x==a-2*r:
        mY=-mY
    if y==b-2*r:
        mX=-mX
onTimer(update,10)

run()
