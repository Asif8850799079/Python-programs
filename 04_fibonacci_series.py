# A series of numbers in which eadch number (fibonacci number) is the sum of the two preceeding numbers.

# 0  1  1  2  3  5  8  13  21  34
# n1 n2
n1 = 0 
n2 = 1
print(n1)
print(n2)

for i in range(2,14):
  sum =n1 + n2
  print(sum) #1
  n1 = n2
  n2 = sum

  