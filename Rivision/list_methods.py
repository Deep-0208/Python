# Creating a sample list
my_list = [10, 20, 30, 40, 50]

# Append: Adds an element to the end
my_list.append(60)
print(my_list)  # [10, 20, 30, 40, 50, 60]

# Extend: Adds elements from an iterable
my_list.extend([70, 80])
print(my_list)  # [10, 20, 30, 40, 50, 60, 70, 80]

# Insert: Inserts element at a specific index
my_list.insert(2, 25)
print(my_list)  # [10, 20, 25, 30, 40, 50, 60, 70, 80]

# Remove: Removes first occurrence of the specified value
my_list.remove(40)
print(my_list)  # [10, 20, 25, 30, 50, 60, 70, 80]

# Pop: Removes and returns element at a given index
popped = my_list.pop(3)
print(popped)   # 30
print(my_list)  # [10, 20, 25, 50, 60, 70, 80]

# Index: Returns the index of the first occurrence
print(my_list.index(50))  # 3

# Count: Counts occurrences of a specified value
print(my_list.count(20))  # 1

# Sort: Sorts the list in ascending order
my_list.sort()
print(my_list)  # [10, 20, 25, 50, 60, 70, 80]

# Reverse: Reverses the list
my_list.reverse()
print(my_list)  # [80, 70, 60, 50, 25, 20, 10]

# Copy: Creates a shallow copy of the list
copy_list = my_list.copy()
print(copy_list)  # [80, 70, 60, 50, 25, 20, 10]

# Clear: Removes all elements
my_list.clear()
print(my_list)  # []