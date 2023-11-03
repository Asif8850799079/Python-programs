# Find the sum of elements in a list

#Approach1: using the sum method

myList = [2,4,5,3,2]
# print(sum(myList))

#Approach2: using for loop with the range()
total = 0
for i in range(0,len(myList)):
  total = total+myList[i]

print(total)