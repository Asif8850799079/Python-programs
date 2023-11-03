# Find the second largest number is a list
# mylist = [70,11,20,4,100]
# output = 70

#Method1:

mylist = [70,11,20,4,100]
# mylist.sort()
# print(mylist)
# print("The second largest number is: ",mylist[-2])

#Method2:
newlist = set(mylist)
newlist.remove(max(newlist))
print(max(newlist))
