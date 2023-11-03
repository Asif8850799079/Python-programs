# Search an element in a list

#Approach1: Using the looping statement

mylist = [1,2,3,4,5,6]

# num = 7
# flag = 0
# for i in mylist:
#   if (i == num):
#     print("Number is found")
#     flag += 1
#     break
# if(flag==0):
#   print("Number not found")

# Approach2: using in operator

num = 5
if (num in mylist):
  print("number found")
else:
  print("number not found")