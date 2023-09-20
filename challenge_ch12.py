# chapter 12 challenge
#1
#shapes:round, oblate, oblong
#class Apple:
#    def __init__(self, w, c, s, j):
#        self.weight = w
#        self.color = c
#        self.shape= s
#        self.juice=j
#        print("Created!")

#A1 = Apple(10, "red", "oblong", "yes")
#print("Weight:", A1.weight)
#print("Color:", A1.color)
#print("Shape:", A1.shape)
#print("Juice:", A1.juice)


#2
#import math

#class Circle:
#    def __init__(self,r):
#        self.radius=r
#        print("created!")

#    def area(self):
#        return math.pi*self.radius**2
               
#circle=Circle(5)
#print("Area:",circle.area())

#3
#class Triangle:
#    def __init__(self,b, h):
#        self.base=b
#        self.height=h
#        print("created!")

#    def area(self):
#        return self.base*self.height/2
               
#triangle=Triangle(3,4)
#print("Area:",triangle.area())

#4
class Hexagon:
    def __init__(self,a,b,c,d,e,f):
        self.length1=a
        self.length2=b
        self.length3=c
        self.length4=d
        self.length5=e
        self.length6=f
        print("created!")

    def calculate_perimeter(self):
        return self.length1+self.length2+\
               self.length3+self.length4+\
               self.length5+self.length6
    
hexagon=Hexagon(3,4,5,6,7,8)
print("Hexagon perimeter:",hexagon.calculate_perimeter())


