# chapter 13 challenge
#1
#class Rectangle:
#    def __init__(self,w, l):
#        self.width=w
#        self.length=l
#        print("created!")

#    def calculate_perimeter(self):
#        return self.width*2+self.length*2
               
#rectangle=Rectangle(3,4)
#print("calculate perimeter of a rectangle:",rectangle.calculate_perimeter())

#class Square:
#    def __init__(self, l):
#        self.length=l
#        print("created!")

#    def calculate_perimeter(self):
#        return self.length*4
               
#square=Square(3)
#print("calculate perimeter of a square:",square.calculate_perimeter())


#2
#class Square:
#    def __init__(self, l):
#        self.length=l
#        print("created!")

#    def area(self):
#        return self.length*self.length
               
#square=Square(3)
#print("calculate area of a square:",square.area())
#print("The area of the square is changeable")
#l=input("Input a square's length:")
#l=int(l)
#square=Square(l)
#print("calculate area of a square:",square.area())

#3
#class Shape:
#    def __init__(self, w,l):
#        self.width=w
#        self.length=l
#        print("created!")

#    def what_am_i(self):
#        print("I am a shape")
#shape=Shape(3,5)
#shape.what_am_i()

#class Square(Shape):
#    pass
#square=Square(3,3)
#square.what_am_i()
#class Rectangle(Shape):
#    pass
#rectangle=Rectangle(3,4)
#rectangle.what_am_i()


#4

class Horse():
    def __init__(self,
               name,
               jockey):
        self.name=name
        self.jockey=jockey

class Rider():
    def __init__(self,name):
        self.name=name

Zac=Rider("Zac PUTTON")
uton=Horse("Exultant", Zac)
print(uton.jockey.name)
    
