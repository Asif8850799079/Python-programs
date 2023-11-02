# 5! = 5*4*3*2*1
# Factorial using the basic for loops 

# num = 5
# factorial = 1

# if num == 0:
#   print("The factorial of 0 is 1")
# elif num<0:
#   print("There is no factorial")
# else:
#   for i in range(1,num+1):
#     factorial = factorial*i

# print("The factorial of the number",num ,"is" ,factorial)

#***************-----------**********

# Factorial using the recursive method
# 5! = 5*4*3*2*1
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(5))