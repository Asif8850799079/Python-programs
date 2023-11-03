# Count the occurances of an element in a list

#Approach1 : using the count method
mylist = [12,4,5,6,4,2,1,7,5,29,4]
print(mylist.count(4))

#Approach2 : using the looping statement
num = 4
count = 0
for elem in mylist:
  if elem == num:
    count += 1

print(f"{num} has occured {count} times")

#Approach3: using counter()
from collections import Counter
x = 12
dic = Counter(mylist) 
print(dic[x])