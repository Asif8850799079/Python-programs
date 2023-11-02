# finding the maximum and minimum in an array
# input: arr[] = {10,20,4}
# output: max=> 20
# output: min=> 4

# 1.Logical approach
# Checking for the maximum value
arr = [1, 2, 35, 4, 5]
# Assume the first element is the maximum
max = arr[0]
n = len(arr)
for i in range(1, n):
    if arr[i] > max:
        max = arr[i]

print("maximum element is",max)

# Checking for the minimum value
arr = [1, 3, 5, 6, 4, 3, 0]
min = arr[0]
n = len(arr)
for i in range(1, n):
    if arr[i] < min:
        min = arr[i]

print("minimum element is",min)
