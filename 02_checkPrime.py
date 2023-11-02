# How to check a number is a prime or not

# Natural number>1
# Which has only 2 factors 1 and itself
# 19 => 1 and 19 => Prime number
# 28 => 1,2,4,7,14,28 => Not a prime number

num = 19
count = 0
if num>1:
  for i in range(1,num+1):
    if (num%i)==0:
      count+=1
  if count == 2:
    print("the number is prime")
  else:
    print("Number is not a prime")

