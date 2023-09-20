# chapter 7 challenge
#1
#lists=["The Walking Dead","Entourage",\
#        "The Sapranos","The Vampire Diaries"]

#for show in lists:
#    print(show)


#2

#for i in range(25,51):
#    print(i)


#3
#lists=["The Walking Dead","Entourage",\
#        "The Sapranos","The Vampire Diaries"]
#i=0
#for show in lists:
#    print(i,show)
#    i +=1


#4
#guess_no_list=["1997","721","831","612","2020","2019","1984","2021"]
#print("I have a set of numbers you can made a guest")
#guess = input ()

#n = 0
#while True:
#    print("Type q to quit, or input a number:")
#    guess = input()
#    if guess == "q":
#        break
#    if guess in guess_no_list:
#        guess==guess_no_list
#        print("correct", guess)
#    if guess not in guess_no_list:
#        guess != guess_no_list
#        print("incorrect", guess)
#        n +=1


#5

list1 = [8,19,148,4]
list2 = [9,1,22,83]
added = []
for i in list1:
    for j in list2:
        added.append(i * j)


print(added)
