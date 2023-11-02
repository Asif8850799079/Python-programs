# To find the length of the list
# Logical approach

mylist = [1,3,54,6,3]
print(mylist)

count = 0

for i in mylist:
  count+=1

print("Length of the list is ",count)

# Python approach build in function

mylist = [1,3,54,6,3,4,5,3]
print(mylist)

print("The length of the list using length method",len(mylist))