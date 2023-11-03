# Reverse words in a string
# input = "welcome to pythn programming"
# output = "programming python to welcome"

string = "welcome to pythn programming"
words = string.split(" ")
print(words)
words = words[::-1]
ouputstr = " ".join(words)
print(ouputstr)
