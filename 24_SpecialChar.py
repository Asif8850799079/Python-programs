# Check String contains special characters
import re

str = "sugarsheikh4656@gmail.com``"
regex = re.compile('[!@#$%^&*()|~`]')
if(regex.search(str)==None):
  print("No special characters in a string")
else:
  print("String contains special characters")