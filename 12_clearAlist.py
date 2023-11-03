#Approach1: using clear() method

mylist = [1,2,3,4]
# print("My list before clear",mylist)
# mylist.clear()
# print("my list after clear",mylist)

#Approach2: initialzes the list with no value

# print("My list before clear",mylist)
# mylist = []
# print("my list after clear",mylist)

#Approach3: using "*=0" this method removes all elements of th list and makes it empty

# print("My list before clear",mylist)
# mylist *=0
# print("my list after clear",mylist)

#Approach4: using del
print("My list before clear",mylist)
del mylist[:]
print("my list after clear",mylist)