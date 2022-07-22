from cmath import sqrt
from numpy import square
def display(): #display at  command line
    
    print("Choose option")
    print("1# Sum X+Y")
    print("2# Multiplicate x+y")
    print("3# The Square  of x ")
    print("4# Take the square root of x ")
class calc:
    def __init__(self,x : float,y : float): #Constructor that prints out text on screen
        self.x = x#  instanciating the variables used in the calculator
        self.y =y
    #methods( a function that belongs to an object) for the calculator 
    def sum(self):
        return self.x+self.y
    def mult(self):
        return self.x*self.y
    def square(self):
        return square(self.x)
    def sqrt(self):
        return sqrt(self.x)
    
display()
z = int(input("Option number #"))
x  = int(input("X value: "))
if z == 1 or z ==  2:
    y  = int(input("y value:"))
else : y=0
    
calc1= calc(x,y)
if z == 1: #if statements to choose options from display
   print(calc1.sum())
if z == 2:
    print(calc1.mult())
if z == 3:
    print(calc1.square())
if z == 4:
    print(calc1.sqrt())
