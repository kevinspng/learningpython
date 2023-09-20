# chapter 4 challenge
#1
#x=input("""Please input an integer and
#the programme gives a square of it:""")
#x= int(x)
#def f(x):
#    return x*x
#f(x)
#print(f(x))

#2
#x=input("your name is:")
#x= str(x)
#print("Nice to meet you")
#print(x)

#3
#a=input("type a number:")
#a=int (a)
#b=input("type a number:")
#b=int (b)
#c=input("type a number:")
#c=int (c)

#def f(a,b,c,d=None,e=None):
#    return a+b+c
    
#print(f(a,b,c))
 
#consulted AI, an improvement
#a=input("type a number:")
#a=int (a)
#b=input("type a number:")
#b=int (b)
#c=input("type a number:")
#c=int (c)
#d=input("type a number:")
#d=int (d)
#e=input("type a number:")
#e=int (e)

#def f(a,b,c,d=0,e=0):
#    result= a+b+c
#    if d is not None:
#     result += d
#    if e is not None:
#     result += e
#    return result
    
#print(f(a,b,c,d,e))

#4
#x=input("type an integer:")
#x=int (x)
#def f(x):
#    if x%2==0:
#    print("the integer is an even integer")
#    else:
#     print("the integer is an odd integer")
#f(x)
#print (x) gets the input integer
#y=x
#def multiple(y):
#    return y*4
#multiple(y)
#print ("the integer mutiply by four is:", multiple (y) )

#5


try:
    x=input("input a number:")
    def _fl(x):
        """
        create a function, and it takes
        the input to a system function,
        i.e. float(), which when taking
        a string will cause a system error
        of ValueError, that why using try-except
        to capture a system error and
        turn to another design message
        """
        x=float(x)
        print("the number in float is:", x)
        return x
    y=_fl(x)
except (ValueError,TypeError, NameError):
    print("It is not a float nor a integer")
    print("It is possibily a string")



#from AI
#try:
#    x = input("Enter a number: ")
#    x = float(x)
#    print("The number is:", x)
#except ValueError:
#    print("The input is not a valid integer.")


    

#6

