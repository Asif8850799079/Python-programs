# Find smallest & largest numbers in a list 

mylist = [2,4,388,12,5]
# Method 1: Sort the list in ascending order and print the first and last elements in the list
# mylist.sort()
# print(mylist)

# print("smallest element is: ",mylist[0])
# print("largest element is: ",mylist[-1])

#Method 2: using min() and max() methods
print("smallest element is: ",min(mylist))
print("largest element is: ",max(mylist))