from graph import *
width=700
height=700
canvasSize(width,height)
brushColor('green')
r=30 #радиус шарика
x = 60
y = 210
c=circle(x, y, r)
mX=1
mY=1

def update():
    global mX
    global mY
    global x
    global y
    '''x = xCoord(c)
    y = yCoord(c)
    x += mX
    y += mY'''

    x += mX
    y += mY

    moveObjectTo(c, x, y)
    if x + 2*r >= width:
        mX *= -1

    if y<=0:
        mY=-mY

    if x<=0:
        mX=-mX

    if y+2*r>=height:
        mY=-mY

onTimer(update,5)

run()
