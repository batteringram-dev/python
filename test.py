
#https://learnpython.com/blog/python-array-vs-list/

arr = {1, 2, 3} #array or set.
list = [1, 2, 3] #list

print(arr)
print(list)

print(type(arr))
print(type(list))

# 1. No duplicates.
arr1 = {1, 1, 2, 3} # no duplicates.
list1 = [1, 1, 2, 2, 3]
print(arr1)
print(list1)

#2. Different data type
arr2 = {1, 2, 1, 2.2}  # cannot hold values of different data types.
list2 = [1, 2, "hello"] # can hold values of different data type.
print(arr2)
print(list2)