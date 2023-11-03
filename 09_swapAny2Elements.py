# program to swap any 2 elements in an array
#input: list = [1,2,3,4],pos1 = 1 , pos2 = 3
#ouput: list = [3,2,1,4]

#Approach1: Simple swap

mylist = [1,2,3,4] # index starts from 0
# print(mylist,"original list")

# pos1,pos2 = 1,3

# mylist[pos1],mylist[pos2] = mylist[pos2],mylist[pos1]
# print(mylist,"updated list")

#Approach2: Using inbuilt list.pop() function
# pos1,pos2 = 1,3
# first_elem = mylist.pop(pos1) #1
# second_elem = mylist.pop(pos2-1) # 2,3,4 

# mylist.insert(pos1,second_elem)
# mylist.insert(pos2,first_elem)

# print(mylist)


# Approach3 : Using tuple
pos1,pos2 = 1,3
get = (mylist[pos1],mylist[pos2])
mylist[pos2],mylist[pos1] =get

print(mylist)