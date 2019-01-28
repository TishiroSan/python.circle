from constants import *
from graph import *
class FieldStub:
    def __init__(self):
        self.color=(100,255,100)
        self.fieldX=0
        self.fieldY=0
        self.x=0
        self.y=0
        penSize(0)
        brushColor(self.color)
        self.object=rectangle(self.x,self.y,self.x+FIELD_SIZE,self.y+FIELD_SIZE)

    def getObject(self):
        return self.object

    def setPosition(self, fieldX, fieldY):
        self.fieldX=fieldX
        self.fieldY =fieldY
        self.x=fieldX*FIELD_SIZE
        self.y= fieldY * FIELD_SIZE
        moveObjectTo(self.object, self.x,self.y)

