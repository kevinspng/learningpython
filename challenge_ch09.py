# chapter 8 challenge
#1

#import os
#suppose the target file
#is on this pathway in linux:
#/home/kevin/Documents/learningPython/street.txt

#os.path.join("home",
#             "kevin",
#             "Documents",
#             "learningPython"
#             "street.txt")
#address=[]
#with open("street.txt","r") as f:
#    address.append(f.read())
#print(address)


#2

# ask for an address code and save it to a file

#with open("address_code.txt","w") as f:
#    address_code=input("Please input an address code:")
#    f.write(address_code)
#    print(address_code)

#3
#import csv
#with open("movies.csv","w", newline='') as f:
#    w=csv.writer(f,delimiter=",")
#    w.writerow(["Top Gun"])
#    w.writerow(["Risky Business"])
#    w.writerow(["Minority Report"])
#    w.writerow(["Titanic"])
#    w.writerow(["The Revenant"])
#    w.writerow(["Inception"])
#    w.writerow(["Training Day"])
#    w.writerow(["Man on Fire"])
#    w.writerow(["Flight"])
    
# 2nd part
#with open("movies.csv", "r") as f:
#    r=csv.reader(f,delimiter=",")
#    for row in r:
#        print(",".join(row))
    
