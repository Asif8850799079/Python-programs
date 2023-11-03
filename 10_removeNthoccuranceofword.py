# remove Nth occurrence of the given word
#input : list = ["geeks", "for" , "geeks"]
#word = geeks , N = 2
#Output: list = ["geeks","for"]

mylist = ["geeks", "for" , "geeks","for","geeks","nigga","geeks"]
word = "geeks"
n = 4

count = 0
for i in range(0,len(mylist)):
  if(mylist[i]==word):
    count+=1 # 1 2
    if (count==n):
      del mylist[i]

print(mylist)