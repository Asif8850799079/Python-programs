# How to clone or copy a list
"""
1.Using slicing technique
2.Using extend() method
3.Using the list() method
4.Using the copy() method
5.Using the list comprehension
"""
# 1.Using slicing technique
mylist = [3,4,5,6,3,2]
# mylistcopy = mylist[:]
# print(mylistcopy)

# 2.Using extend() method
# newlist = []
# newlist.extend(mylist)
# print(newlist)

# 3.Using the list() method
# newList = list(mylist)
# print(newList)

# 4.Using the copy() method
# mylist_copy = mylist.copy()
# print(mylist)

# 5.Using the list comprehension
mylist_copy = [i for i in mylist]
print(mylist_copy)