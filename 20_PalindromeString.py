# Program to find the palindrome string
# Input : madam
# output : palindrome

# Method1
#1)Find reverse of string
#2)Check if reverse and original are same or not

string = 'reverse'
reversedString = string[::-1]

if string == reversedString:
  print("Its palindrome")
else:
  print("Not a palindrome") 