# Substring present in a given string 
# The find() method finds the first occurance of the specified value
# The find() method returns -1 if the value is not found

string = "welcome to python programming"
sub_str = "python"
output = string.find(sub_str)

if(string.find(sub_str)==-1):
  print("Not found")
else:
  print("found")