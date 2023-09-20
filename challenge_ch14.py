# chapter 14 challenge
1

#class Square():
#    squ=[]
    
#    def __init__(self, l):
#        self.length=l
#        print("created!")
#        self.squ.append(self.length)
#        print(Square.squ)


#squ1=Square(1)
#squ2=Square(2)
#squ3=Square(3)



#2
#class Square():
    
#    def __init__(self, l):
#        self.length=l
#        print("created!")

#    def print_size(self):
#        print("The square is {} by {} by {} by {}".format((self.length),
#                                                 (self.length),
#                                                 (self.length),
#                                                 (self.length)))
#s1=Square(29)
#s1.print_size()

#3
class Stock:
    def __init__(self,name):
        self.name=name

Google=Stock('Google')
Alphabet=Google
print("Google is Alphabet:",Google is Alphabet)

TSM=Stock('TSM')
Taiwan_Semiconductor_Manufacturing=TSM
print("Google is TSM:",Google is TSM)


    
