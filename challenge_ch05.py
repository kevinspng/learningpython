# chapter 5 challenge
#1
#f_hk_musicans=["Andy Lau","Allen Tam","Kenny B","Maria Cordero"]
#print(f_hk_musicans)

#2
#my_uk_residences=("121 McLeod Rd 51.2916,0.06496","326 Spinner House 53.47113,2.28058")
#print(my_uk_residences)
#xxx McLeod Rd
#xx.2916,0.06496
#xxx Spinner House
#xx.47113,2.28058

#3
#my_attributes=dict()
#my_attributes["name"]=("kevin")
#my_attributes["age"]=("63")
#my_attributes["education"]=("degree")
#my_attributes["height"]=("173")
#my_attributes["eye"]=("brown")
#my_attributes["ethnic"]=("hongkonger")
#my_attributes["favourite colour"]=("white, yellow and blue")
#my_attributes["favourite author"]=("George Orwell","JK Rowling")
#my_attributes["favourite fruit"]=("apple")
#my_attributes["favourite music"]=("sound of music")
#my_attributes["favourite movie"]=("harry potter")
#my_attributes["favourite food"]=("HK style")
#my_attributes["favourite athlete"]=("Micheal Phelps","Mark Spitz")
#my_attributes["favourite hobby"]=("learning n studying n investing")

#4
#my_attributes=dict()
#my_attributes["name"]=("kevin")
#my_attributes["age"]=("63")
#my_attributes["education"]=("degree")
#my_attributes["height"]=("173")
#my_attributes["eye"]=("brown")
#my_attributes["ethnic"]=("hongkonger")
#my_attributes["favourite colour"]=("white, yellow and blue")
#my_attributes["favourite author"]=("George Orwell","JK Rowling")
#my_attributes["favourite fruit"]=("apple")
#my_attributes["favourite music"]=("sound of music")
#my_attributes["favourite movie"]=("harry potter")
#my_attributes["favourite food"]=("HK style")
#my_attributes["favourite athlete"]=("Micheal Phelps","Mark Spitz")
#my_attributes["favourite hobby"]=("learning n studying n investing")

#print("""l would like to introduce myself. You could ask my attributes,
#         by words, for example, name, age, education,..etc]:""")

#x = input("")
#x= str(x)
#if x in my_attributes:
#    my_attributes= my_attributes[x]
#    print(my_attributes)
#else:
#    print ("the attributes not found")

#5

#Simon_and_Garfunkel=("The Sound of Silence","Bridge Over Troubled Water","Homeward Bound",
#                     "The Boxer","Mrs Robinson","Scarborough Fair/Canticle")

#The_Beatles=("When I’m Sixty-Four","With a Little Help from My Friends","Magical Mystery Tour",
#             "Yellow Submarine","Day Tripper","A Hard Day’s Night")

#Tat_Ming_Pair=("The Story of the Stone","I'm Waiting For Your Return","Faith, Hope & Love",
#              "How Great Thou Art","Dance, Dance, Dance")

#singers=(Simon_and_Garfunkel,The_Beatles,Tat_Ming_Pair)

#lists={singers[0]:Simon_and_Garfunkel,singers[1]:The_Beatles,singers[2]:Tat_Ming_Pair}

#print("""l have grouped some famous songs to singer. You could test it.
#         Please input a song name""")
#x = input("")
#x= str(x)
#my code
#if x in lists:
#    singers= lists[x]
#    print(singers)
#else:
#    print ("the song not identified")
#AI code still no good come back later
Simon_and_Garfunkel = ("The Sound of Silence", "Bridge Over Troubled Water", "Homeward Bound",
                       "The Boxer", "Mrs Robinson", "Scarborough Fair/Canticle")

The_Beatles = ("When I’m Sixty-Four", "With a Little Help from My Friends", "Magical Mystery Tour",
               "Yellow Submarine", "Day Tripper", "A Hard Day’s Night")

Tat_Ming_Pair = ("The Story of the Stone", "I'm Waiting For Your Return", "Faith, Hope & Love",
                 "How Great Thou Art", "Dance, Dance, Dance")

singers = (Simon_and_Garfunkel, The_Beatles, Tat_Ming_Pair)

lists = {singers[0]: Simon_and_Garfunkel, singers[1]: The_Beatles, singers[2]: Tat_Ming_Pair}

print("""I have grouped some famous songs to singers. You could test it.
         Please input a song name""")
x = input("")
x = str(x)
if x in lists.values():
    for singer, songs in lists.items():
        if x in songs:
            print(singer)
else:
    print("The song was not identified.")










#The Sound of Silence
#Bridge Over Troubled Water
#Homeward Bound
#The Boxer
#Mrs Robinson
#Scarborough Fair/Canticle

#The Beatles
#When I’m Sixty-Four
#With a Little Help from My Friends
#Magical Mystery Tour
#Yellow Submarine
#Day Tripper
#A Hard Day’s Night

#Tat Ming Pair
#The Story of the Stone
#I'm Waiting For Your Return
#Faith, Hope & Love
#How Great Thou Art
#Dance, Dance, Dance


#6
In Python, a set is an unordered collection of unique elements. It is one of the four built-in data types in Python, along with lists, tuples, and dictionaries ¹. 

A set is defined using curly braces `{}` or the `set()` constructor. The elements in a set must be immutable, meaning that they cannot be changed once they are added to the set. Sets are useful for performing mathematical operations such as union, intersection, and difference ¹.

Here is an example of how to create a set:

```python
# Create a set
my_set = {1, 2, 3}
```

In this example, we are creating a set named `my_set` that contains the elements `1`, `2`, and `3`.

I hope this helps!

Source: Conversation with Bing, 12/09/2023
(1) Python Sets - W3Schools. https://www.w3schools.com/python/python_sets.asp.
(2) Python Sets - GeeksforGeeks. https://www.geeksforgeeks.org/python-sets/.
(3) Sets in Python – Real Python. https://realpython.com/python-sets/.
(4) 5. Data Structures — Python 3.11.5 documentation. https://docs.python.org/3/tutorial/datastructures.html.
