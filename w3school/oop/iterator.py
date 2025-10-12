import sys

# 1. Using a list with for loop
my_list = list(range(1_000_000)) 
# creates a list with 1 million elements
# print(my_list)
print("Memory of list:", sys.getsizeof(my_list), "bytes")

# 2. Using an iterator
my_iter = iter(range(1_000_000))  # creates an iterator
print("Memory of iterator:", sys.getsizeof(my_iter), "bytes")
print(my_iter)
print(next(my_iter))
print(next(my_iter))