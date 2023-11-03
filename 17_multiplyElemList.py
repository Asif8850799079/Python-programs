# Multiply all the numbers in the list

# #method 1: Traversal
mylist = [3,5,2]
# result = 1
# for i in mylist:
#   result = result * i

# print(result)

#Method 2: using numpy.prod() *install numpy package
import numpy

result = numpy.prod(mylist)
print(result)