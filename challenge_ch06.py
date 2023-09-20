# chapter 6 challenge
#1
#Camus="Camus"
#print(Camus[0])
#print(Camus[1])
#print(Camus[2])
#print(Camus[3])
#print(Camus[4])

#2

#print("""you are preparing a story line and shall send to someone,
#input a theme:""")
#s1=input()
#print("input a person name:")
#n2=input()
#sentence="""Yesterday I wrote a "{}". I sent it to {}.""".format(s1, n2)
#print(sentence)


#3
#s="aldous Huxley was born in 1894"
#s=s.capitalize()
#print(s)

#4
#print("""you are preparing a record of job report,
#you need information on location,
#name, and time.""")

#print ("a location, please:")
#w1=input()
#print("input a name:")
#n2=input()
#print("input a time:")
#t3=input()   
#sentence="""A job at "{}" was fixed by {}, between {}.""".format(w1,n2,t3)
#print(sentence)

#5

#a="The "
#b="fox "
#c="jumped "
#d="over "
#e="the "
#f="fence"
#g="."

#sentence=a+b+c+d+e+f+g
#print(sentence)


#6
#sen="A Screaming comes across the sky."
#sen=sen.replace("s","$")
#print(sen)

#7

#w="Hemingway"
#n=w.index("m")
#print(n)


#8 not tested, no txt file textbook found
#b=textbook
#b=b.index["\"\""]
#print(b)


#9
#a="three "
#print(a+a+a)
#print(a*3)

#10
s="It was a bright cold day in April, and the clocks were striking thirteen."
n=s.index(",")
print(n)
s1=s[0:n]
print(s1)
