# chapter 17 challenge
#1 bash
 
#cd $python_projects
#grep Dutch zen.txt
#Although that way may not be obvious at first unless you're Dutch.

#2
#echo Arizona 479, 501, 890. California 209, 213, 650. |grep [[:digit:]]
    

#3
import re

string="The ghost that says boo haunts the loo."

m=re.findall("[bl]oo",string,re.IGNORECASE)

print(m)
