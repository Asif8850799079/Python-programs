# 1. Swapping the numbers using the temp variable
num1 = 10
num2 = 5
temp = num1 #10
num1=num2 #5
num2=temp #10

print(num1)
print(num2)

# 2. Python way of swapping

a = 5
b =6

a , b = b ,a 
print(b)
print(a)